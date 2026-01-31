import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuração da Página
st.set_page_config(layout="wide", page_title="Dashboard de Salários", page_icon="💰")

# 2. Carregamento dos Dados
arquivo_csv = os.path.join(os.path.dirname(__file__), 'dados_imersao_final.csv')
df = pd.read_csv(arquivo_csv)

# 3. Barra Lateral (Filtros)
st.sidebar.header("Filtros")
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", ["Todos"] + list(df['ano'].unique()))
senioridade_selecionada = st.sidebar.multiselect("Senioridade", df['senioridade'].unique(), default=df['senioridade'].unique())

# Aplicando Filtros
df_filtrado = df[df['senioridade'].isin(senioridade_selecionada)]
if ano_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['ano'] == ano_selecionado]

# 4. Título e KPIs
st.title("💰 Dashboard de Salários na Área de Dados")
st.markdown("Explore como variam os salários por cargo, experiência e localização.")

col1, col2, col3 = st.columns(3)
col1.metric("Total de Vagas", len(df_filtrado))
col2.metric("Salário Médio (Anual)", f"US$ {df_filtrado['usd'].mean():.2f}")
col3.metric("Maior Salário", f"US$ {df_filtrado['usd'].max():.2f}")

# 5. Gráficos
col_graf1, col_graf2 = st.columns(2)

# Gráfico 1: Barras
fig_barras = px.bar(df_filtrado.groupby('cargo')[['usd']].mean().sort_values('usd', ascending=False).head(10).reset_index(),
                    x='usd', y='cargo', orientation='h', title="Top 10 Cargos (Salário Médio)", color='usd')
col_graf1.plotly_chart(fig_barras, use_container_width=True)

# Gráfico 2: Mapa
df_mapa = df_filtrado.groupby('empresa_loc')[['usd']].mean().reset_index()
fig_mapa = px.choropleth(df_mapa, locations='empresa_loc', locationmode='ISO-3', color='usd',
                         title="Média Salarial por País", color_continuous_scale="Viridis")
col_graf2.plotly_chart(fig_mapa, use_container_width=True)

# 6. Tabela de Dados
with st.expander("Ver Base de Dados Completa"):
    st.dataframe(df_filtrado)