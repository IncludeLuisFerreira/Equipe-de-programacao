# Primeira versão da conexão de um cliente
# Ainda não tem banco de dados então salvei em arquivos separados

import socket

file_name = 'bd.csv'
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
            
            with open(file_name, 'a') as arquivo:
                arquivo.write(message + "\n")
                

        except ValueError:
            print("Formato de mensagem inválido...")
            continue

cliente_socket.close()
server.close()
