import pandas as pd
import sqlite3
from pathlib import Path

# === Caminhos ===
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "gs2025.db"
conn = sqlite3.connect(DB_PATH)

# === Lê a base de todas as regiões ===
df = pd.read_sql("SELECT * FROM indicadores_udh_all", conn)

# === Verificação de colunas necessárias ===
colunas_necessarias = ["idhm", "ren1", "t_banagua", "t_lixo", "t_agua", "t_rmaxidoso"]
for col in colunas_necessarias:
    if col not in df.columns:
        raise KeyError(f"🛑 Coluna obrigatória '{col}' não encontrada.")

# === Cálculo dos componentes ===

# Infraestrutura (quanto maior, melhor; IGV usa o inverso)
df["infraestrutura"] = 1 - (df["t_banagua"]/100 + df["t_lixo"]/100 + df["t_agua"]/100) / 3

# Normalizações
df["ren1_norm"] = df["ren1"] / 100
df["t_rmaxidoso_norm"] = df["t_rmaxidoso"] / 100

# === Cálculo final do IGV ===
df["igv"] = (
    0.3 * (1 - df["idhm"]) +
    0.3 * df["ren1_norm"] +
    0.2 * df["infraestrutura"] +
    0.2 * df["t_rmaxidoso_norm"]
)

# Seleção final de colunas para exportar
colunas_exportar = [
    "cod_id", "udh_atlas", "nome_udh", "nome_mun", "nome_uf",
    "regiao", "idhm", "ren1", "infraestrutura", "t_rmaxidoso", "igv"
]
df_resultado = df[colunas_exportar]

# === Salvar no banco ===
df_resultado.to_sql("igv_resultado_all", conn, if_exists="replace", index=False)
conn.close()

print("✅ IGV calculado e salvo na tabela 'igv_resultado_all'.")
