import streamlit as st

st.write('# Classificação de Iris')
st.write('## Exemplo com comprimento de petala e sepala.')

st.sidebar.write('### Parametros')
st.sidebar.slider('Comprimento da Sépala', 4.0, 8.0, 5.8, 0.1)
st.sidebar.slider('Comprimento da Pétala', 0.9, 7.0, 3.8, 0.1)