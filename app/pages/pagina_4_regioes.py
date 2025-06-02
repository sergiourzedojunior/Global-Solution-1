# app/pages/pagina_4_regioes.py

import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Comparativo Regional", layout="wide")
st.title("🌎 Comparativo Regional de IGV")

# Caminho do banco
DB_PATH = Path(__file__).resolve().parent.parent.parent / "db" / "gs2025.db"

# Carregamento com cache
@st.cache_data
def carregar_dados():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM igv_resultado_all", conn)
    conn.close()
    return df

df = carregar_dados()

# === Ranking de Regiões por IGV Médio ===
df_ranking = (
    df.groupby("regiao")[["igv"]]
    .mean()
    .reset_index()
    .sort_values("igv", ascending=False)
    .round(3)
)

# Separar Top 5 piores e melhores
piores_regioes = df_ranking.head(5)
melhores_regioes = df_ranking.tail(5).sort_values("igv")

# Exibição do ranking
st.subheader("📊 Regiões com os Piores IGVs (média)")
st.dataframe(piores_regioes.rename(columns={"igv": "IGV médio"}))

st.subheader("🌟 Regiões com os Melhores IGVs (média)")
st.dataframe(melhores_regioes.rename(columns={"igv": "IGV médio"}))

# === Boxplot geral por região ===
st.subheader("📦 Distribuição do IGV por Região")
fig = px.box(
    df,
    x="regiao",
    y="igv",
    points="outliers",
    title="Distribuição do IGV por Região",
    color="regiao"
)
fig.update_layout(xaxis_title="Região", yaxis_title="IGV", showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# === Mapa interativo (futuro ou opcional) ===
# Pode-se adicionar uma visualização com shapefile posteriormente
