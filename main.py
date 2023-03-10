import pandas as pd
from datetime import datetime

#================== MESCLAGEM DOS ARQUIVOS =================#

# carregar os arquivos CSV em DataFrames separados
netflix_df = pd.read_csv("netflix_titles.csv")
prime_df = pd.read_csv("amazon_prime_titles.csv")

# combinar os DataFrames em um único DataFrame
merged_df = pd.concat([netflix_df, prime_df])

# salvar o DataFrame consolidado em um novo arquivo CSV
merged_df.to_csv("merged_titles.csv", index=False)

#========= TOP 10 atores/atrizes (mais repete) =============#

# carregar o arquivo CSV consolidado em um DataFrame
merged_df = pd.read_csv("merged_titles.csv")

# contar a frequência dos valores na coluna "cast"
cast_counts = merged_df["cast"].value_counts()

# selecionar os 10 valores mais comuns
top_cast = cast_counts.head(10)

# imprimir os 10 valores mais comuns
print("Top 10 atores/atrizes:")
print(top_cast)
print()

#========= TOP 5 países =============#

# contar a frequência dos valores na coluna "country"
country_counts = merged_df["country"].value_counts()

# selecionar os 5 valores mais comuns
top_countries = country_counts.head(5)

# imprimir os 5 valores mais comuns
print("Top 5 países:")
print(top_countries)
print()

#======== Mês com mais adição na Netflix ============#

# carregar o arquivo CSV "netflix_titles.csv" em um DataFrame
netflix_df = pd.read_csv("netflix_titles.csv")

# filtrar a coluna "date_added" para remover os valores nulos
netflix_df = netflix_df[netflix_df["date_added"].notna()]

# extrair o nome do mês da coluna "date_added"
month_list = netflix_df["date_added"].astype(str).str.split().str[0].tolist()

# converter o nome do mês em um número de mês
month_num_list = [datetime.strptime(str(month), "%B").month for month in month_list]

# criar uma série com os números dos meses e seus nomes
month_series = pd.Series(month_num_list).map(lambda x: datetime.strptime(str(x), "%m").strftime("%B"))

# contar a frequência dos meses na série
month_counts = month_series.value_counts()

# imprimir o mês mais comum
most_common_month = month_counts.idxmax()
print("O mês mais comum na coluna 'date_added' é:", most_common_month)
print()

#==================== Quantidade Comédia =====================#

# carregar o arquivo merged_titles.csv em um DataFrame
df = pd.read_csv("merged_titles.csv")

# contar quantas vezes a palavra "Comedy" aparece na coluna "listed_in"
comedy_count = df["listed_in"].str.contains("Comedy").sum()

# imprimir o resultado
print("A palavra 'Comedy' aparece", comedy_count, "vezes na coluna 'listed_in'.")
print()

#============== Listagem de todos os gêneros ==================#

# carregar o arquivo merged_titles.csv em um DataFrame
df = pd.read_csv("merged_titles.csv")

# obter a lista de valores únicos na coluna "listed_in"
listed_in_list = df["listed_in"].unique().tolist()

# imprimir a lista de valores únicos
print("Lista de gèneros:")
for elementos in listed_in_list:
  print(elementos)
print()

#================== Frequência TV Show =================#

# carregar o arquivo merged_titles.csv em um DataFrame
df = pd.read_csv("merged_titles.csv")

# contar quantas vezes a palavra "Comedy" aparece na coluna "listed_in"
comedy_count = df["listed_in"].str.contains("TV Shows").sum()

# imprimir o resultado
print("A palavra 'TV Shows' aparece", comedy_count, "vezes na coluna 'listed_in'.")
print()

#================== Frequência Movies =================#

# carregar o arquivo merged_titles.csv em um DataFrame
df = pd.read_csv("merged_titles.csv")

# contar quantas vezes a palavra "Comedy" aparece na coluna "listed_in"
comedy_count = df["listed_in"].str.contains("Movies").sum()

# imprimir o resultado
print("A palavra 'Movies' aparece", comedy_count, "vezes na coluna 'listed_in'.")
print()