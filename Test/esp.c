#include <ESP8266WiFi.h>
#include <PubSubClient.h>   // Nova biblioteca para o mqtt
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Samuel";
const char* password = "password";

const char* host = "192.168.211.196";  // Atualize este IP se necessário
const int port = 50000;                // Porta do servidor

WiFiClient client;

void setup() {
  Serial.begin(9600);
  dht.begin();

  // Conecta ao Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Conectando ao Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado ao Wi-Fi!");
  Serial.print("Endereço IP do ESP8266: ");
  Serial.println(WiFi.localIP());

  // Tenta conectar ao servidor na inicialização
  if (client.connect(host, port)) {
    Serial.println("Conectado ao servidor!");
  } else {
    Serial.println("Falha ao conectar ao servidor.");
  }
}

void loop() {
  float umidade = dht.readHumidity();
  float temperatura = dht.readTemperature();
  if (isnan(umidade) || isnan(temperatura)) {
    Serial.println("Falha ao ler o sensor DHT11!");
    return;
  }

  // Verifica se está conectado ao servidor, se não, tenta reconectar
  if (!client.connected()) {
    Serial.println("Reconectando ao servidor...");
    if (client.connect(host, port)) {
      Serial.println("Reconectado ao servidor!");
    } else {
      Serial.println("Falha ao reconectar ao servidor.");
      delay(5000);
      return;
    }
  }

  // Envia os dados com um delimitador de fim de mensagem
  client.print("Umidade: ");
  client.print(umidade);
  client.print(" %\n");
  client.print("Temperatura: ");
  client.print(temperatura);
  client.print(" °C\n");

  Serial.println("Dados enviados.");

  delay(2000);  // Envia dados a cada 2 segundos
}