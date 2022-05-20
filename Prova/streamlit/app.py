import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write('# Prova 1')
st.write('## Predição de cancer de mama.')

st.sidebar.write('### Parametros')

with open('./streamlit/objetos2.pkl', 'rb') as arquivo:
    ss, dtc = pickle.load(arquivo)

