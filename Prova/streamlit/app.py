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
dimencao_fracional_0 = st.sidebar.slider('dimencao fracional 0', 0.04, 0.10, 0.06, 0.01)

raio_1 = st.sidebar.slider('raio 1', 0.11, 3.0, 0.40, 0.01)
textura_1 = st.sidebar.slider('textura 1', 0.30, 5.00, 2.86, 0.05)
perimetro_1 = st.sidebar.slider('perimetro 1', 0.7, 22.0, 2.86, 0.05)
area_1 = st.sidebar.slider('area 1', 6.0, 542.2, 40.3, 0.10)
suavizacao_1 = st.sidebar.slider('suavizacao 1', 0.001, 0.031, 0.007, 0.001)
compactacao_1 = st.sidebar.slider('compactacao 1', 0.002,  0.135, 0.025)
concavidade_1 = st.sidebar.slider('concavidade 1', 0.00 ,  0.396 ,  0.032)
pontos_concavos_1 = st.sidebar.slider('pontos concavos 1',  0.00,  0.05,  0.01)
simetria_1 = st.sidebar.slider('simetria 1',  0.007,  0.078,  0.020, 0.001)
dimencao_fracional_1 = st.sidebar.slider('dimencao fracional 1',  0.001,  0.030,  0.004, 0.01)

raio_2 = st.sidebar.slider('raio 2', 7.5, 36.0, 4.8, 0.1)
textura_2 = st.sidebar.slider('textura 2', 12.02, 49.54, 25.67, 0.1)
perimetro_2 = st.sidebar.slider('perimetro 2', 50.41, 251.20, 107.26, 10.0)
area_2 = st.sidebar.slider('area 2', 185.2, 4254.0, 880.58)
suavizacao_2 = st.sidebar.slider('suavizacao 2', 0.07, 0.22, 0.13, 0.01)
compactacao_2 = st.sidebar.slider('compactacao 2', 0.020, 1.060, 0.254, 0.005)
concavidade_2 = st.sidebar.slider('concavidade 2', 0.00, 1.260, 0.272, 0.005)
pontos_concavos_2 = st.sidebar.slider('pontos concavos 2', 0.00, 0.30, 0.12, 0.01)
simetria_2 = st.sidebar.slider('simetria 2', 0.15, 0.70, 0.30, 0.05)
dimencao_fracional_2 = st.sidebar.slider('dimencao fracional 2', 0.055, 0.210, 0.085, 0.005)

with open('./streamlit/objetos2.pkl', 'rb') as arquivo:
    ss, dtc = pickle.load(arquivo)

estrutura = {
  'raio_0' : raio_0,
  'textura_0' : textura_0,
  'perimetro_0' : perimetro_0,
  'area_0' : area_0,
  'suavizacao_0' : suavizacao_0,
  'compactacao_0' : compactacao_0,
  'concavidade_0' : concavidade_0,
  'pontos_concavos_0' : pontos_concavos_0,
  'simetria_0' : simetria_0,
  'dimencao_fracional_0' : dimencao_fracional_0,

  'raio_1' : raio_1,
  'textura_1' : textura_1,
  'perimetro_1' : perimetro_1,
  'area_1' : area_1,
  'suavizacao_1' : suavizacao_1,
  'compactacao_1' : compactacao_1,
  'concavidade_1' : concavidade_1,
  'pontos_concavos_1' : pontos_concavos_1,
  'simetria_1' : simetria_1,
  'dimencao_fracional_1' : dimencao_fracional_1,

  'raio_2' : raio_2,
  'textura_2' : textura_2,
  'perimetro_2' : perimetro_2,
  'area_2' : area_2,
  'suavizacao_2' : suavizacao_2,
  'compactacao_2' : compactacao_2,
  'concavidade_2' : concavidade_2,
  'pontos_concavos_2' : pontos_concavos_2,
  'simetria_2' : simetria_2,
  'dimencao_fracional_2' : dimencao_fracional_2,
}

df = pd.DataFrame(estrutura, index=[0])

st.write('### Parametros de entrada:')
st.write(df)