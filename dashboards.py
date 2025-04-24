import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Dashboard de Vendas📊") #título do dashboard


df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date") #ordenando o dataframe pela data

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())


df_filtred = df[df["Month"] == month] #filtrando o dataframe para o mês selecionado

# df_filtred #exibindo o dataframe filtrado na tela

col1, col2 = st.columns(2) #dividindo a tela em duas colunas
col3, col4, col5 = st.columns(3) #dividindo a tela em três colunas

fig_date = px.bar(df_filtred, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True) #exibindo o gráfico na segunda coluna

#tipo de produto
fig_prods = px.bar(df_filtred, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prods, use_container_width=True) #exibindo o gráfico na primeira coluna

#Contribuição de cada cidade para o faturamento total 
city_total = df_filtred.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(df_filtred, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True) #exibindo o gráfico na primeira coluna

#Tipo de pagamento
fig_kind = px.pie(df_filtred, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True) #exibindo o gráfico na segunda coluna

#Avaliação Média
city_total = df_filtred.groupby("City")[["Rating"]].sum().reset_index()
fig_rating = px.bar(df_filtred, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True) #exibindo o gráfico na segunda coluna
