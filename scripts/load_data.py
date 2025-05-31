import pandas as pd
import sqlite3
from pathlib import Path

# === 1. Caminhos base
BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"
DB_DIR = BASE_DIR / "db"
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "gs2025.db"

# === 2. Conexão com SQLite
conn = sqlite3.connect(DB_PATH)

# === 3. Inicialização
tabela_destino = "indicadores_udh_all"
dados_total = []

# === 4. Loop sobre pastas 'dados_*'
for pasta in DADOS_DIR.iterdir():
    if pasta.is_dir() and pasta.name.startswith("dados_"):
        regiao_nome = pasta.name.replace("dados_", "").lower()

        # Busca recursiva por qualquer planilha contendo 'UDH' no nome
        arquivos = list(pasta.glob("**/*UDH*.xlsx"))
        if not arquivos:
            print(f"⚠️ Nenhum arquivo UDH encontrado em: {pasta}")
            continue

        # Usa o primeiro arquivo encontrado
        arquivo = arquivos[0]
        print(f"📥 Lendo {arquivo.name} da região '{regiao_nome}'")

        try:
            df = pd.read_excel(arquivo)
        except Exception as e:
            print(f"❌ Erro ao ler {arquivo.name}: {e}")
            continue

        # Padroniza nomes de colunas
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace(r"[^\w_]", "", regex=True)
        )

        # Adiciona coluna com o nome da região
        df["regiao"] = regiao_nome
        dados_total.append(df)

# === 5. Concatena tudo e salva no SQLite
if dados_total:
    df_final = pd.concat(dados_total, ignore_index=True)
    df_final.to_sql(tabela_destino, conn, if_exists="replace", index=False)
    print(f"✅ Dados de {len(dados_total)} regiões salvos na tabela '{tabela_destino}'.")
else:
    print("⚠️ Nenhuma região foi carregada com sucesso.")

conn.close()
