from paho.mqtt import client as paho
import time
import requests
import sys

BROKER = 'localhost'  # IP do servidor que irá receber as mensagens
PORT = 1883
TOPIC = 'Sensor'

# Cria o cliente MQTT e se conecta ao broker
client = paho.Client() 
if client.connect(BROKER, PORT, 60) != 0:
    print("Couldn't connect to mqtt broker")
    sys.exit(1)
    

api_key = '9d3e90a83727f54955434d982b108fb0'

# URL da API para Poços de Caldas
api_urls = {
    'pocos': f'http://api.openweathermap.org/data/2.5/weather?q=Poços+de+Caldas,BR&appid={api_key}&units=metric',
}

# Função para processar a resposta da API e obter temperatura e umidade
def process_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Gera exceção para erros HTTP
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

try:
    while True:
        for name, url in api_urls.items():
            temperatura, umidade = process_api(url)
            
            if temperatura is not None and umidade is not None:
                # Converte os valores de temperatura e umidade em inteiros para publicação
                temperatura = int(temperatura * 100)
                umidade = int(umidade * 100)
        
                # Formata a mensagem para ser publicada
                mensagem = f"{temperatura},{umidade}\n"
                
                # Publica a mensagem no tópico especificado
                client.publish(TOPIC, mensagem)
                
                print(f"Dados enviados: {mensagem.strip()}")
        
        # Aguarda 2 segundos antes da próxima leitura e publicação
        time.sleep(2)

except KeyboardInterrupt:
    print("Cliente finalizado pelo usuário.")

finally:
    # Desconecta do broker MQTT de forma limpa
    client.disconnect()
    print("Desconectado do broker.")
