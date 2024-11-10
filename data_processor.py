# Primeira versão da conexão de um cliente
# Ainda não tem banco de dados então salvei em arquivos separados

import socket

HOST = '0.0.0.0'
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor escutando em {HOST}:{PORT}...")

cliente_socket, client_address = server.accept()
print(f"Conexão estabelecida com {client_address}")

buffer = ""
while True:
    data = cliente_socket.recv(1024).decode()
    if not data:
        print("Conexão perdida!")
        break
    
    buffer += data
    
    while "\n" in buffer:
        message, buffer = buffer.split("\n", 1)
        
        try:
            temperatura, umidade = message.split(",")
            
            with open("temperatura.cqv", "a") as temp_file:
                temp_file.write(temperatura + "\n")
                
            with open("umidade.cqv", "a") as umid_file:
                umid_file.write(umidade + "\n")
                
            print(f"Temperatura: {temperatura}, Umidade: {umidade} - Dados salvos")
        
        except ValueError:
            print("Formato de mensagem inválido...")
            continue

cliente_socket.close()
server.close()
