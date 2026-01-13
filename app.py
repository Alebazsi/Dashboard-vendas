import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da Página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# 2. Carregar os Dados
df = pd.read_csv("dados_vendas.csv")

# 3. Barra Lateral (Filtros)
st.sidebar.header("🔍 Filtros")
estado_selecionado = st.sidebar.multiselect(
    "Selecione o Estado:",
    options=df["Estado"].unique(),
    default=df["Estado"].unique()
)

categoria_selecionada = st.sidebar.multiselect(
    "Selecione a Categoria:",
    options=df["Categoria"].unique(),
    default=df["Categoria"].unique()
)

# Aplicar filtros no DataFrame (Tabela)
df_filtrado = df.query(
    "Estado == @estado_selecionado & Categoria == @categoria_selecionada"
)

# 4. Página Principal
st.title("📊 Dashboard de Performance de Vendas")
st.markdown("---")

# Calcular Métricas (KPIs)
total_vendas = (df_filtrado["Preco"] * df_filtrado["Quantidade"]).sum()
qtd_produtos = df_filtrado["Quantidade"].sum()
media_venda = total_vendas / qtd_produtos if qtd_produtos > 0 else 0

# Exibir Cartões de Métricas
col1, col2, col3 = st.columns(3)
col1.metric("💰 Faturamento Total", f"R$ {total_vendas:,.2f}")
col2.metric("📦 Produtos Vendidos", qtd_produtos)
col3.metric("💲 Ticket Médio", f"R$ {media_venda:,.2f}")

st.markdown("---")

# 5. Gráficos Interativos
col_graf1, col_graf2 = st.columns(2)

# Gráfico 1: Faturamento por Estado
grafico_estados = px.bar(
    df_filtrado, 
    x="Estado", 
    y="Preco", 
    color="Estado", 
    title="Faturamento por Estado"
)
col_graf1.plotly_chart(grafico_estados, use_container_width=True)

# Gráfico 2: Vendas por Categoria 
grafico_categoria = px.pie(
    df_filtrado, 
    names="Categoria", 
    values="Quantidade", 
    title="Distribuição por Categoria"
)
col_graf2.plotly_chart(grafico_categoria, use_container_width=True)

# 6. Exibir a Tabela de Dados
st.subheader("📋 Base de Dados Detalhada")
st.dataframe(df_filtrado)