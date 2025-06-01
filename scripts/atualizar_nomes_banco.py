# atualizar_nomes_banco.py
import sqlite3
import pandas as pd
from pathlib import Path

# Caminho do banco
DB_PATH = Path(__file__).resolve().parent.parent / "db" / "gs2025.db"

# Mapeamento de nomes
mapa_nomes_regioes = {
    "sp": "São Paulo (SP)",
    "rj": "Rio de Janeiro (RJ)",
    "bh": "Belo Horizonte (MG)",
    "bs": "Baixada Santista (SP)",
    "campinas": "Campinas (SP)",
    "cuiaba": "Cuiabá (MT)",
    "curitiba": "Curitiba (PR)",
    "df": "Distrito Federal (DF)",
    "goiania": "Goiânia (GO)",
    "manaus": "Manaus (AM)",
    "natal": "Natal (RN)",
    "fortaleza": "Fortaleza (CE)",
    "salvador": "Salvador (BA)",
    "recife": "Recife (PE)",
    "sl": "São Luís (MA)",
    "teresina_timon": "Teresina/Timon (PI/MA)",
    "maceio": "Maceió (AL)",
    "belem": "Belém (PA)",
    "pa": "Porto Alegre (RS)",
    "petrolina_juazeiro": "Petrolina/Juazeiro (PE/BA)",
    "valedoparaiba": "Vale do Paraíba (SP)",
    "vitoria": "Vitória (ES)",
    "sorocaba": "Sorocaba (SP)",
    "florianopolis": "Florianópolis (SC)"
}

# Conectar ao banco
conn = sqlite3.connect(DB_PATH)

# Ler os dados
df = pd.read_sql("SELECT * FROM igv_resultado_all", conn)

# Substituir os nomes
df["regiao"] = df["regiao"].replace(mapa_nomes_regioes)

# Salvar de volta
df.to_sql("igv_resultado_all", conn, if_exists="replace", index=False)
conn.close()

print("✅ Nomes das regiões atualizados diretamente na tabela 'igv_resultado_all'.")
