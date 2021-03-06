import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write('# Classificação de Iris')
st.write('## Exemplo com comprimento de petala e sepala.')

st.sidebar.write('### Parametros')
comp_sepala = st.sidebar.slider('Comprimento da Sépala', 4.0, 8.0, 5.8, 0.1)
larg_sepala = st.sidebar.slider('Largura da Sépala', 2.0, 5.0, 1.0, 0.1)
comp_petala = st.sidebar.slider('Comprimento da Pétala', 0.9, 7.0, 3.8, 0.1)
larg_petala = st.sidebar.slider('Largura da Petala', 0.1, 3.0, 1.0, 0.1)

with open('./streamlit/objetos2.pkl', 'rb') as arquivo:
    ss, dtc = pickle.load(arquivo)

estrutura = { 'comp_sepala': comp_sepala, 'larg_sepala': larg_sepala, 'comp_petala': comp_petala, 'larg_petala': larg_petala }

df = pd.DataFrame(estrutura, index=[0])

st.write('### Parametros de entrada:')
st.write(df)

df = ss.transform(df)
st.write(df)

predicao = dtc.predict(df)
st.write(f"Classe dessa flor é: **{predicao[0]}**")

mapeamento = {
  0: 'Iris-setosa',
  1: 'Iris-versicolor',
  2: 'Iris-virginica',
}

predicao_proba = dtc.predict_proba(df)
predicao_proba = pd.DataFrame(predicao_proba)
predicao_proba.rename(mapeamento, axis=1, inplace=True)

st.write(f"Probabilidade:")
st.write(predicao_proba)
