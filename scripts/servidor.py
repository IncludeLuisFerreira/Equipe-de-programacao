from paho.mqtt import client as paho
import sys

file_name = '../folders/bd.csv'

def on_message(client, userdata, message):
   print(f"{message.topic}: {message.payload}")

server = paho.Client()
server.on_message = on_message

if server.connect("localhost", 1883, 60) != 0:
    print("Erro ao conectar ao servidor MQTT")
    sys.exit(1)

server.subscribe("Sensor")
print(f"Servidor escutando no tópico 'Sensor' em localhost: 1883...")

try:
    server.loop_forever()
except KeyboardInterrupt:
    print("Desconectando do servidor...")
finally:
    server.disconnect()
    print("Servidor desconectado.")
