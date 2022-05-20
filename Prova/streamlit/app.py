import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write('# Prova 1')
st.write('## Predição de cancer de mama.')

st.sidebar.write('### Parametros')

raio_0 = st.sidebar.slider('raio 0', 6.0, 30.0, 14.1, 0.1)
textura_0 = st.sidebar.slider('textura 0', 9.0, 40.0, 4.3, 0.1)
perimetro_0 = st.sidebar.slider('perimetro 0', 43.0, 190.0, 24.2, 0.1)
area_0 = st.sidebar.slider('area 0', 140.0, 2501.0, 352.0, 1.0)
suavizacao_0 = st.sidebar.slider('suavizacao 0', 0.03, 0.17, 0.01, 0.01)
compactacao_0 = st.sidebar.slider('compactacao 0', 0.01, 0.35, 0.05, 0.01)
concavidade_0 = st.sidebar.slider('concavidade 0', 0.00, 0.43, 0.07, 0.01)
pontos_concavos_0 = st.sidebar.slider('pontos concavos 0', 0.00, 0.20, 0.04, 0.01)
simetria_0 = st.sidebar.slider('simetria 0', 0.10, 0.30, 0.02, 0.01)
dimencao_fracional_0 = st.sidebar.slider('dimencao fracional 0')

raio_1 = st.sidebar.slider('raio 1')
textura_1 = st.sidebar.slider('textura 1')
perimetro_1 = st.sidebar.slider('perimetro 1')
area_1 = st.sidebar.slider('area 1')
suavizacao_1 = st.sidebar.slider('suavizacao 1')
compactacao_1 = st.sidebar.slider('compactacao 1')
concavidade_1 = st.sidebar.slider('concavidade 1')
pontos_concavos_1 = st.sidebar.slider('pontos concavos 1')
simetria_1 = st.sidebar.slider('simetria 1')
dimencao_fracional_1 = st.sidebar.slider('dimencao fracional 1')

raio_2 = st.sidebar.slider('raio 2')
textura_2 = st.sidebar.slider('textura 2')
perimetro_2 = st.sidebar.slider('perimetro 2')
area_2 = st.sidebar.slider('area 2')
suavizacao_2 = st.sidebar.slider('suavizacao 2')
compactacao_2 = st.sidebar.slider('compactacao 2')
concavidade_2 = st.sidebar.slider('concavidade 2')
pontos_concavos_2 = st.sidebar.slider('pontos concavos 2')
simetria_2 = st.sidebar.slider('simetria 2')
dimencao_fracional_2 = st.sidebar.slider('dimencao fracional 2')

with open('./streamlit/objetos2.pkl', 'rb') as arquivo:
    ss, dtc = pickle.load(arquivo)

