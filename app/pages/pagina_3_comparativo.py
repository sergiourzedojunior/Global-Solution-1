# app/pages/pagina_3_comparativo.py

import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title="IGV - Comparativo Extremos", layout="wide")
st.title("📊 Comparativo de Vulnerabilidade: Melhores vs Piores IGVs")

# === Caminho e conexão com banco ===
DB_PATH = Path(__file__).resolve().parent.parent.parent / "db" / "gs2025.db"

@st.cache_data
def carregar_dados():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM igv_resultado_all", conn)
    conn.close()
    return df

df = carregar_dados()

# === Selecionar extremos ===
N = 10

# Seleciona os N melhores (menor IGV)
melhores = df.sort_values("igv", ascending=True).head(N).copy()
melhores["Grupo"] = "Melhores IGV"

# Seleciona os N piores (maior IGV)
piores = df.sort_values("igv", ascending=False).head(N).copy()
piores["Grupo"] = "Piores IGV"

# Concatena os dois grupos
df_comp = pd.concat([melhores, piores], ignore_index=True)

# === Indicadores ===
indicadores = {
    "idhm": "IDHM",
    "ren1": "Renda até 1 SM (%)",
    "infraestrutura": "Infraestrutura precária (1 - acesso)",
    "t_rmaxidoso": "Idosos isolados (%)"
}

# === Gráficos comparativos ===
st.subheader("📉 Comparativo por Indicador")

for col, label in indicadores.items():
    fig = px.box(df_comp, x="Grupo", y=col, points="all", title=f"{label}")
    fig.update_layout(yaxis_title=label, xaxis_title="")
    st.plotly_chart(fig, use_container_width=True)

# === Tabela comparativa ===
st.subheader("📄 Estatísticas médias dos grupos")
df_medias = df_comp.groupby("Grupo")[list(indicadores.keys())].mean().round(3).rename(columns=indicadores)
st.dataframe(df_medias)

# === Detalhamento das UDHs ===
with st.expander("🔎 Ver detalhes das UDHs analisadas"):
    st.dataframe(df_comp[["Grupo", "nome_udh", "nome_mun", "regiao", "igv"] + list(indicadores.keys())].round(3))

