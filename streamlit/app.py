import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write('# Classificação de Iris')
st.write('## Exemplo com comprimento de petala e sepala.')

st.sidebar.write('### Parametros')
comp_sepala = st.sidebar.slider('Comprimento da Sépala', 4.0, 8.0, 5.8, 0.1)
comp_petala = st.sidebar.slider('Comprimento da Pétala', 0.9, 7.0, 3.8, 0.1)

with open('./streamlit/objetos.pkl', 'rb') as arquivo:
    ss, dtc = pickle.load(arquivo)

estrutura = { 'comp_sepala': comp_sepala, 'comp_petala': comp_petala }

df = pd.DataFrame(estrutura, index=[0])

st.write('### Parametros de entrada:')
st.write(df)

df = ss.transform(df)
st.write(df)

predicao = dtc.predict(df)
st.write(f"Classe dessa flor é: **{predicao[0]}**")

predicao_proba = dtc.predict_proba(df)
st.write(f"Probabilidade: {predicao_proba[0]}")
