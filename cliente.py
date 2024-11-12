import socket
import time
import random
import requests

HOST = '127.0.0.1'  # IP do servidor, no caso o computador que irá receber 
PORT = 50000        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

api_key = '9d3e90a83727f54955434d982b108fb0'

# URL da API para Poços de Caldas
api_urls = {
    'pocos': f'http://api.openweathermap.org/data/2.5/weather?q=Poços+de+Caldas,BR&appid={api_key}&units=metric',
}

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

try:
    while True:
        
        for name, url in api_urls.items():
            temperatura, umidade = process_api(url)
            
            if temperatura is not None and umidade is not None:
                # Multiplica por 100 e converte para inteiros
                temperatura = int(temperatura * 100)
                umidade = int(umidade * 100)
        
        mensagem = f"{temperatura},{umidade}\n"
        
        client_socket.sendall(mensagem.encode())
        
        print(f"Dados enviados: {mensagem.strip()}")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("Cliente finalizado.")

finally:
    client_socket.close()
