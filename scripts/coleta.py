import requests
import time
from pymongo import MongoClient

# Chave pessoal API da OpenWeatherMap
api_key = '9d3e90a83727f54955434d982b108fb0'
MONGO_URI = 'mongodb+srv://prgluis:123@luis.do00k.mongodb.net/?retryWrites=true&w=majority&appName=Luis'

# URL da API para Poços de Caldas
api_urls = {
    'pocos': f'http://api.openweathermap.org/data/2.5/weather?q=Poços+de+Caldas,BR&appid={api_key}&units=metric',
}

try:
    # Conectando ao MongoDB
    cliente = MongoClient(MONGO_URI)
    db = cliente['Extensao']  # Nome correto do banco de dados
    collection = db['sensores']  # Nome correto da coleção
except Exception as e:
    pass

# Função para processar a resposta da API e obter temperatura e umidade
def process_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Coleta erro
        data = response.json()  # Converte a resposta em JSON
        
        # Obtém a temperatura e umidade do JSON
        temperatura = data['main']['temp']  # Temperatura em graus Celsius
        umidade = data['main']['humidity']  # Umidade em porcentagem
        print("Temperatura:", temperatura)  # Exibe a temperatura para depuração
        print("Umidade:", umidade)  # Exibe a umidade para depuração

        return temperatura, umidade
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None, None

# Função para escrever dados no arquivo CSV

def main():
    # Nome do arquivo de saída
    file_name = 'folders/bd.csv'
    
    # Cria o arquivo e adiciona o cabeçalho na primeira vez
    
    while True:
        # Processa cada URL da API
        for name, url in api_urls.items():
            temperatura, umidade = process_api(url)
            
            if temperatura is not None and umidade is not None:
                # Multiplica por 100 e converte para inteiros
                temperatura = int(temperatura * 100)
                umidade = int(umidade * 100)
                
                # Cria uma linha de dados para o CSV
                dados = {
                    "tipo": "temperatura",
                    "dado": temperatura,
                    "tipo": "umidade",
                    "dado":umidade
                }

                insert_Dado = collection.insert_one(dados)
                print(f"Dado inserido: {insert_Dado.inserted_id}")
                
                # Adiciona a linha ao arquivo
               
        print("Dados salvos no arquivo")

        # Aguarda 10 minutos (600 segundos) antes de coletar os dados novamente
        time.sleep(1)

if __name__ == "__main__":
    main()
