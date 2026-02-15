# ETL Automatizado com Python

Pipeline simples de ETL desenvolvido para prática de fundamentos em Engenharia de Dados.

## 📌 Contexto

Este projeto simula um processo de ingestão e tratamento de dados de vendas, aplicando transformações básicas para geração de um dataset estruturado.

## 🔄 Etapas do Pipeline

1. Leitura do dataset bruto (CSV)
2. Tratamento de valores nulos
3. Conversão de tipos de dados
4. Enriquecimento com nova coluna (ano)
5. Geração de arquivo tratado

## 🛠 Tecnologias

- Python
- Pandas

## 📂 Estrutura do Projeto

data/raw → dados brutos  
data/processed → dados tratados  
scripts → lógica do ETL  

## ▶ Como executar

```bash
pip install -r requirements.txt
python scripts/etl.py