import streamlit as st
from functions.plot_ts import plot

st.title('Historico de contacoes')
st.write('Veja o historico de contações das empresas.')

ticker = st.siderbar.text_input('Escolha o ticker:', value = 'AAPL')

fig = plot(ticker)
st.plotly_char(fig)