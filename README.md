# Global Solution 2025 — FIAP

Projeto de Análise de Vulnerabilidade Socioeconômica para Eventos Extremos, desenvolvido em Python e SQLite como parte do desafio Global Solution da FIAP.

## 📌 Objetivo

Identificar regiões metropolitanas e municípios brasileiros com maior vulnerabilidade social frente a desastres naturais, utilizando indicadores do Atlas Brasil, IPS 2025 e CEMADEN.

## 🧰 Tecnologias

- Python 3.10+
- SQLite
- Pandas, GeoPandas
- Streamlit (visualização)
- GitHub (versionamento)
- VS Code

## 📂 Estrutura

- `/dados/` → Dados brutos (ignorado no Git)
- `/db/` → Banco de dados SQLite
- `/scripts/` → Scripts de ETL, análise, dashboards
- `/notebooks/` → Exploração inicial e validações

## 🚀 Execução

```bash
pip install -r requirements.txt
python scripts/load_data.py
