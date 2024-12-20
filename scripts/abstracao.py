import csv
from collections import deque
import statistics
import os

def calcular_estatisticas_ultimas_linhas(file_name_entrada, file_name_saida, intervalo=10):
    temperaturas = deque(maxlen=intervalo)
    umidades = deque(maxlen=intervalo)
    
    with open(file_name_entrada, 'r') as file:
        reader = list(csv.DictReader(file))  
        
        if not reader:
            print("O arquivo de entrada está vazio!")
            return

        for row in reader[-intervalo:]:
            temperatura = int(row['Temperatura']) / 100
            umidade = int(row['Umidade']) / 100
            temperaturas.append(temperatura)
            umidades.append(umidade)
    
    if len(temperaturas) == intervalo and len(umidades) == intervalo:
        try:
            moda_temperatura = int(statistics.mode(temperaturas)) * 100
        except statistics.StatisticsError:
            moda_temperatura = "Sem moda"  
            
        moda_umidade = int(statistics.mode(umidades)) * 100 if len(set(umidades)) > 1 else "Sem moda"
        
        mediana_temperatura = int(statistics.median(temperaturas)) * 100
        mediana_umidade = int(statistics.median(umidades)) * 100
        
        desvio_temperatura = int(statistics.stdev(temperaturas)) * 100 if len(temperaturas) > 1 else 0
        desvio_umidade = int(statistics.stdev(umidades)) * 100 if len(umidades) > 1 else 0
        
        estatisticas = {
            'Moda_Temperatura': str(moda_temperatura),
            'Moda_Umidade': str(moda_umidade),
            'Mediana_Temperatura': f"{mediana_temperatura}",
            'Mediana_Umidade': f"{mediana_umidade}",
            'Desvio_Padrao_Temperatura': f"{desvio_temperatura}",
            'Desvio_Padrao_Umidade': f"{desvio_umidade}"
        }

        file_exists = os.path.exists(file_name_saida)

        with open(file_name_saida, 'a', newline='') as file:  
            writer = csv.DictWriter(file, fieldnames=estatisticas.keys())
            
            if not file_exists or file.tell() == 0:
                writer.writeheader()
            
            writer.writerow(estatisticas)  

        print(f"Estatísticas das últimas {intervalo} leituras calculadas e adicionadas no arquivo {file_name_saida}:")
        print(f"Moda Temperatura: {moda_temperatura}")
        print(f"Moda Umidade: {moda_umidade}")
        print(f"Mediana Temperatura: {mediana_temperatura:.2f}")
        print(f"Mediana Umidade: {mediana_umidade:.2f}")
        print(f"Desvio Padrão Temperatura: {desvio_temperatura:.2f}")
        print(f"Desvio Padrão Umidade: {desvio_umidade:.2f}")
    else:
        print(f"O arquivo possui menos de {intervalo} leituras, estatísticas não calculadas.")

file_name_entrada = 'folders/bd.csv'   
file_name_saida = 'folders/abstracao.csv'  

calcular_estatisticas_ultimas_linhas(file_name_entrada, file_name_saida)
