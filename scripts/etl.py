import pandas as pd

# Leitura do arquivo bruto
df = pd.read_csv("data/raw/vendas.csv")

# Transformações
df["valor"] = df["valor"].fillna(0)  # Preenche valores nulos
df["data"] = pd.to_datetime(df["data"])  # Converte para datetime

# Cria nova coluna
df["ano"] = df["data"].dt.year

# Salva arquivo tratado
df.to_csv("data/processed/vendas_tratadas.csv", index=False)

print("ETL executado com sucesso!")