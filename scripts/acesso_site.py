import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://tempo.inmet.gov.br/CondicoesRegistradas" 

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    temperatura = soup.find("span", {"id": "temperatura"}).text
    umidade = soup.find("span", {"id": "umidade"}).text
    
    data = {
        "Data e Hora": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Temperatura": [temperatura],
        "Umidade": [umidade]
    }
    df = pd.DataFrame(data)
    
    df.to_csv("dados_inmet.csv", mode="a", index=False, header=False)
    print("Dados salvos com sucesso!")
else:
    print(f"Erro ao acessar o site: {response.status_code}")