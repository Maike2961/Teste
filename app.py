import pandas as pd


df = pd.read_csv("./file/vendas.csv", encoding='ISO-8859-1', sep=';')

df["Faturamento"] = df['Preco_Unitario'] * df['Quantidade']

print(df)

maior_fatura = df["Faturamento"].max()
menor_fatura = df["Faturamento"].min()

print()
print(f"A maior fatura é de {maior_fatura} e o menor é de {menor_fatura}")
    
    
