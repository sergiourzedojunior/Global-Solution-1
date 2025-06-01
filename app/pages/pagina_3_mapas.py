# app/pages/pagina_3_mapas.py
import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px

# Caminho fixo e real do banco
DB_PATH = Path(__file__).resolve().parent.parent.parent / "db" / "gs2025.db"

# === Título da Página ===
st.set_page_config(page_title="IGV - Mapa", layout="wide")
st.title("🗺️ Mapa de Calor do IGV por Região Metropolitana")

# === Carregar dados da base igv_resultado_all ===
@st.cache_data
def carregar_dados():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM igv_resultado_all", conn)
    conn.close()
    return df

df = carregar_dados()

# === Filtro lateral por região ===
regioes = sorted(df["regiao"].dropna().unique())
regiao_sel = st.selectbox("Selecione a região metropolitana:", regioes)
df_filtrado = df[df["regiao"] == regiao_sel]

# === Validação de coordenadas ===
if "latitude" not in df.columns or "longitude" not in df.columns:
    st.warning("❌ Dados de latitude e longitude não estão disponíveis na base de dados.")
else:
    st.markdown("### 🌐 Mapa de calor do IGV na região selecionada")
    fig = px.scatter_mapbox(
        df_filtrado,
        lat="latitude",
        lon="longitude",
        color="igv",
        hover_name="nome_udh",
        hover_data={"igv": True, "nome_mun": True},
        color_continuous_scale="Reds",
        size_max=12,
        zoom=9,
        height=600,
    )
    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig, use_container_width=True)
