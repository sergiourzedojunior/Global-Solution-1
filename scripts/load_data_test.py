import pandas as pd
import sqlite3
from pathlib import Path

# === 1. CONFIGURAÇÃO DE CAMINHOS ===
BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados" / "dados_vitoria" / "base final RM Vitória"
ARQUIVO_EXCEL = DADOS_DIR / "RM 63200 Vitória - Base UDH 2000_2010.xlsx"

DB_DIR = BASE_DIR / "db"
DB_DIR.mkdir(parents=True, exist_ok=True)  # Garante que a pasta db exista
DB_PATH = DB_DIR / "gs2025.db"

# === 2. LEITURA DOS DADOS ===
print(f"📥 Lendo arquivo: {ARQUIVO_EXCEL}")
df = pd.read_excel(ARQUIVO_EXCEL)

# === 3. LIMPEZA BÁSICA ===
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^\w_]", "", regex=True)
)

# Remove colunas totalmente vazias (se houver)
df.dropna(axis=1, how='all', inplace=True)

# === 4. INSERÇÃO NO SQLITE ===
print(f"📦 Conectando ao banco: {DB_PATH}")
conn = sqlite3.connect(DB_PATH)


print(f"🔍 Dimensões do DataFrame: {df.shape}")

TABELA = "indicadores_udh"
print(f"💾 Inserindo dados na tabela: {TABELA}")
df.to_sql(TABELA, conn, if_exists='replace', index=False)

conn.close()
print("✅ Dados inseridos com sucesso em db/gs2025.db.")
