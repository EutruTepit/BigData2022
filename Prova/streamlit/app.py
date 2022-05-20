import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write('# Prova 1')
st.write('## Predição de cancer de mama.')

st.sidebar.write('### Parametros')

raio_0 = st.sidebar.slide('raio 0')
textura_0 = st.sidebar.slide('textura 0')
perimetro_0 = st.sidebar.slide('perimetro 0')
area_0 = st.sidebar.slide('area 0')
suavizacao_0 = st.sidebar.slide('suavizacao 0')
compactacao_0 = st.sidebar.slide('compactacao 0')
concavidade_0 = st.sidebar.slide('concavidade 0')
pontos_concavos_0 = st.sidebar.slide('pontos concavos 0')
simetria_0 = st.sidebar.slide('simetria 0')
dimencao_fracional_0 = st.sidebar.slide('dimencao fracional 0')

raio_1 = st.sidebar.slide('raio 1')
textura_1 = st.sidebar.slide('textura 1')
perimetro_1 = st.sidebar.slide('perimetro 1')
area_1 = st.sidebar.slide('area 1')
suavizacao_1 = st.sidebar.slide('suavizacao 1')
compactacao_1 = st.sidebar.slide('compactacao 1')
concavidade_1 = st.sidebar.slide('concavidade 1')
pontos_concavos_1 = st.sidebar.slide('pontos concavos 1')
simetria_1 = st.sidebar.slide('simetria 1')
dimencao_fracional_1 = st.sidebar.slide('dimencao fracional 1')

raio_2 = st.sidebar.slide('raio 2')
textura_2 = st.sidebar.slide('textura 2')
perimetro_2 = st.sidebar.slide('perimetro 2')
area_2 = st.sidebar.slide('area 2')
suavizacao_2 = st.sidebar.slide('suavizacao 2')
compactacao_2 = st.sidebar.slide('compactacao 2')
concavidade_2 = st.sidebar.slide('concavidade 2')
pontos_concavos_2 = st.sidebar.slide('pontos concavos 2')
simetria_2 = st.sidebar.slide('simetria 2')
dimencao_fracional_2 = st.sidebar.slide('dimencao fracional 2')

with open('./streamlit/objetos2.pkl', 'rb') as arquivo:
    ss, dtc = pickle.load(arquivo)

