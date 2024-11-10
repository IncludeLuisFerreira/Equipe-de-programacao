import socket
import time
import random

HOST = '192.168.127.11'  # IP do servidor, no caso o computador que irá receber 
PORT = 50000        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        temperatura = round(random.uniform(20.0, 30.0), 2)
        umidade = round(random.uniform(30.0, 70.0), 2)
        
        mensagem = f"{temperatura},{umidade}\n"
        
        client_socket.sendall(mensagem.encode())
        
        print(f"Dados enviados: {mensagem.strip()}")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("Cliente finalizado.")

finally:
    client_socket.close()
