import pandas as pd


""" Lendo o arquivo CSV, decodificando o arquivo ,separando as colunas com SEP """
df = pd.read_csv("./file/vendas.csv", encoding='ISO-8859-1', sep=';')

""" Criando uma nova coluna e multiplição as colunas de preco com quantidade uma por uma, sem a necessidade de fazer um loop """
df["Faturamento"] = df['Preco_Unitario'] * df['Quantidade']

print(df)

""" descobrindo quais são os maiores e menores faturamentos com os metodos max e min"""
maior_fatura = df["Faturamento"].max()
menor_fatura = df["Faturamento"].min()

print()
print(f"A maior fatura é de {maior_fatura} e o menor é de {menor_fatura}")
    
    
