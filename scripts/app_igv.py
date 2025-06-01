import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px

# === Configurações iniciais ===
st.set_page_config(page_title="Análise de IGV por UDH", layout="wide")
st.title("📊 Análise de Vulnerabilidade Socioeconômica (IGV)")

# Caminho do banco de dados
DB_PATH = Path("db/gs2025.db").resolve()

# === Conecta ao banco e carrega os dados ===
@st.cache_data

def carregar_dados():
    con = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM igv_resultado_all", con)
    con.close()
    return df

df = carregar_dados()

# === Filtros ===
regioes = sorted(df["regiao"].unique())
regiao_sel = st.sidebar.selectbox("Selecione a região:", ["Todas"] + regioes)

if regiao_sel != "Todas":
    df = df[df["regiao"] == regiao_sel]

# === Métricas ===
col1, col2, col3 = st.columns(3)
col1.metric("📊 Total de UDHs", f"{len(df):,}".replace(",", "."))
col2.metric("🔢 IGV Médio", f"{df['igv'].mean():.3f}".replace(".", ","))
col3.metric("🥇 IGV Máximo", f"{df['igv'].max():.3f}".replace(".", ","))

# === Tabela ===
st.subheader("🔢 Top 10 UDHs mais vulneráveis")
df_top = df.sort_values("igv", ascending=False).head(10)
st.dataframe(df_top[["nome_udh", "nome_mun", "regiao", "igv"]], height=300)

# === Gráfico ===
st.subheader("🔺 Distribuição do IGV")
fig = px.histogram(df, x="igv", nbins=40, color_discrete_sequence=["indianred"])
fig.update_layout(xaxis_title="IGV", yaxis_title="Contagem", bargap=0.1)
st.plotly_chart(fig, use_container_width=True)

# === Mapa (futuro) ===
# st.subheader("🗺️ Visualização geográfica (em breve)")
