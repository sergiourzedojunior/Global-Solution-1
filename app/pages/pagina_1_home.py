# app/pages/pagina_1_home.py
import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

from scripts.ajustar_nomes_regioes import mapa_nomes_regioes

# === Configurações da página ===
st.set_page_config(page_title="IGV - Índice de Vulnerabilidade", layout="wide")

st.title("📊 Índice Geral de Vulnerabilidade (IGV)")

# === Texto introdutório ===
st.markdown("""
O **IGV - Índice Geral de Vulnerabilidade** é um indicador sintético que busca representar, de forma integrada, a vulnerabilidade socioeconômica e estrutural das Unidades de Desenvolvimento Humano (UDHs) das Regiões Metropolitanas brasileiras.

Ele é construído a partir de quatro dimensões principais:

- ✨ **Educação e desenvolvimento humano** (IDHM)
- 💸 **Renda per capita baixa** (proporção de domicílios com renda de até 1 SM per capita)
- 🌊 **Infraestrutura urbana precária** (saneamento, lixo e água encanada)
- ♥️ **Grupos vulneráveis** (presença de idosos sem rede de apoio familiar)

Quanto **maior o IGV**, **maior é a vulnerabilidade** daquela UDH.
""")

# === Conexão com banco ===
DB_PATH = Path(__file__).resolve().parent.parent.parent / "db" / "gs2025.db"

@st.cache_data
def carregar_dados():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM igv_resultado_all", conn)
    conn.close()
    return df


df = carregar_dados()

# Substituir nomes de regiões
df["regiao"] = df["regiao"].replace(mapa_nomes_regioes)


# === Mapa estático com distribuição do IGV por região ===
st.subheader("🌍 Mapa Estático: Distribuição do IGV por Região Metropolitana")

# Agrupa IGV médio por região para visualização simples
df_grouped = df.groupby("regiao")["igv"].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=df_grouped.values, y=df_grouped.index, palette="Reds_r", ax=ax)
ax.set_title("IGV Médio por Região Metropolitana", fontsize=14)
ax.set_xlabel("IGV Médio")
ax.set_ylabel("Região Metropolitana")
st.pyplot(fig)
