import pandas as pd
import sqlite3
from pathlib import Path

# === 1. Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "gs2025.db"
conn = sqlite3.connect(DB_PATH)

# === 2. Lê dados da tabela
df = pd.read_sql("SELECT * FROM indicadores_udh", conn)

# === 3. Calcula indicadores derivados (com normalização)
df["infraestrutura"] = 1 - (df["t_banagua"]/100 + df["t_lixo"]/100 + df["t_agua"]/100) / 3
df["ren1_norm"] = df["ren1"] / 100
df["t_rmaxidoso_norm"] = df["t_rmaxidoso"] / 100

# === 4. Cálculo do IGV com pesos
df["igv"] = (
    0.3 * (1 - df["idhm"]) +
    0.3 * df["ren1_norm"] +
    0.2 * df["infraestrutura"] +
    0.2 * df["t_rmaxidoso_norm"]
)

# === 5. Seleciona colunas úteis para salvar
colunas_resultado = [
    "cod_id", "udh_atlas", "nome_udh", "nome_mun", "nome_uf",
    "idhm", "ren1", "infraestrutura", "t_rmaxidoso", "igv"
]
df_resultado = df[colunas_resultado]

# === 6. Grava no banco
df_resultado.to_sql("igv_resultado", conn, if_exists="replace", index=False)
conn.close()

print("✅ IGV calculado e salvo na tabela 'igv_resultado'.")
