# importar pacotes
import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

# Carregar o arquivo com os dados
df = pd.read_csv('criminalidade_sp_2.csv')

# Criando dashboard com título e descrição
st.title("Criminalidade em São Paulo")
st.markdown(
    """
    A **criminalidade** é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de Ciências de Dados conseguimos 
    entender melhor o que está acontecendo e gerar insights que direcionem ações capazes de diminuir os 
    índices de criminalidade.
    """
)

# Criando uma sidebar, com opção para carregar tabela com dados
st.sidebar.info("Foram carregadas {} linhas.".format(df.shape[0]))


# Exibir os top 5 registro do dataframe
st.subheader("Tabela de dados")
st.dataframe(df.head(5))

if st.checkbox("Ver tabela de dados completa"):
    st.header("Raw Data")
    st.write(df)

# Criando um mapa de criminalidade
st.subheader("Mapa de criminalidade do estado de São Paulo")
st.map(df)


# Criando um slider para selecionar parâmetro
st.subheader("Valor de prejuízo ocasionado pelo crime")
value = st.slider("Valor (R$)", float(df.valor_prejuizo.min()), 10000., (10.0,100.0))

# Filtrando os dados

dados = df[df.valor_prejuizo.between(left=value[0], right=value[1])]

# Plotando a distribuição dos dados

f = px.histogram(dados, x="valor_prejuizo", nbins=100, title="Distribuição de Valor de Prejuízo")
f.update_xaxes(title="Valor de Prejuízo")
f.update_yaxes(title="Total de Crimes")
st.plotly_chart(f)














