# 🛡️ Sentinela Social

**FIAP - Global Solution 2025 - 1º Semestre**  
**Aluno responsável:** Sergio Urzedo Junior – RM561396  

---

## 🎯 Objetivo do Projeto

Desenvolver uma aplicação web que permita **monitorar, classificar e comparar a vulnerabilidade socioeconômica** de regiões metropolitanas brasileiras, com base em dados prontos e públicos, sem depender de sensores ou predição climática.

---

## 🧠 O que foi desenvolvido

O projeto **Sentinela Social** é uma aplicação em Python (via Streamlit) conectada a um banco de dados SQLite que consolida indicadores de vulnerabilidade em nível de UDH (Unidade de Desenvolvimento Humano). Com isso, o sistema permite:

- Visualizar o **IGV (Índice Geral de Vulnerabilidade)** por região metropolitana;
- Consultar as UDHs mais vulneráveis em cada região;
- Comparar **UDHs com melhores e piores indicadores** em diversos critérios sociais;
- Analisar a **distribuição do IGV por estado (UF)** e região metropolitana.

---

## 📚 Base de Dados e Fontes

Os dados utilizados são públicos e foram consolidados previamente em um banco local `gs2025.db`. As principais fontes utilizadas foram:

- **Atlas da Vulnerabilidade Social (IPEA)**  
  Indicadores de IDHM, infraestrutura, idosos, renda.  
  https://ivs.ipea.gov.br/index.php/pt/

- **IBGE Cidades e Estados**  
  Base geográfica e estatística nacional.  
  https://www.ibge.gov.br

- **Malhas territoriais do IBGE** (shapefiles UFs e municípios)  
  https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais.html

- **Portal Brasileiro de Dados Abertos**  
  https://dados.gov.br/

Foi utilizado um banco consolidado `gs2025.db`, contendo a tabela `igv_resultado_all` com os seguintes campos:

- `nome_udh`, `nome_mun`, `regiao`, `nome_uf`  
- `igv`: índice calculado com base em:
  - IDHM
  - Proporção de domicílios com renda ≤ 1 SM
  - Falta de acesso à infraestrutura básica
  - Presença de idosos sem apoio familiar

---

## 🧩 Funcionalidades por Página

### Página 1 – Visão Geral
- Apresentação do conceito de IGV
- Mapa estático com ranking de IGV médio por região metropolitana

### Página 2 – Análise Detalhada
- Filtros por região metropolitana
- Tabela com top 10 UDHs mais vulneráveis
- Métricas globais
- Histograma da distribuição do IGV

### Página 3 – Comparativo Extremos
- Comparação entre as 10 UDHs mais e menos vulneráveis
- Boxplots por indicador (IDHM, renda, infraestrutura, idosos)
- Tabela comparativa de estatísticas médias

### Página 4 – Comparativo Regional
- Ranking de IGV médio por região metropolitana
- Destaque para 5 piores e 5 melhores regiões
- Boxplot da distribuição do IGV por região

---

## 🧪 Tecnologias Utilizadas

| Tecnologia      | Uso                                                       |
|-----------------|-----------------------------------------------------------|
| Python + Pandas | Leitura, tratamento e agregação de dados                  |
| SQLite          | Armazenamento do banco `gs2025.db` com todos os indicadores |
| Streamlit       | Interface web interativa                                  |
| Plotly / Matplotlib / Seaborn | Geração dos gráficos comparativos            |
| GeoPandas       | Análise geográfica complementar (não usada no app final)  |

---

## 🖼️ Protótipos e Telas

Todas as telas foram implementadas no próprio app Streamlit. Os gráficos e tabelas podem ser utilizados como protótipos na apresentação em PDF:

- Mapa de calor por região
- Histograma do IGV
- Boxplots comparativos
- Tabelas interativas por UDH e região

---

## ✅ Conclusão

O projeto **Sentinela Social** entrega uma ferramenta funcional de apoio à análise de vulnerabilidade social em regiões urbanas, utilizando exclusivamente dados públicos e tecnologias acessíveis. Sua interface simples permite que tomadores de decisão visualizem e comparem áreas críticas para melhor direcionamento de políticas públicas.

---

## 🎬 Link do Pitch (YouTube)

> [INSERIR LINK AQUI QUANDO PRONTO]
