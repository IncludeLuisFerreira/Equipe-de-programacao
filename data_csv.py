import pandas as pd

df = pd.read_csv('dados.csv')

media_umidade = df['umidade'].mean()
moda_umidade = df['umidade'].mode()
mediana_umidade = df['umidade'].median()    # segundo o Celso não faz sentido
desvio_padrao_umidade = df['umidade'].std(ddof=0)
print(f'A média é {media_umidade}')
print(f'A moda é {moda_umidade.values}')
print(f'A mediana é {mediana_umidade}')
print(f'A desvio padrão é {desvio_padrao_umidade:.3f}')
df.loc[0,'media_umidade'] = media_umidade
df.to_csv("dados.csv", index=False)