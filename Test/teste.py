from pymongo import MongoClient

# URI com configuração explícita de SSL
MONGO_URI = 'mongodb+srv://prgluis:123@luis.do00k.mongodb.net/?retryWrites=true&w=majority&appName=Luis'

try:
    # Conectando ao MongoDB
    cliente = MongoClient(MONGO_URI)
    db = cliente['Extensao']  # Nome correto do banco de dados
    collection = db['sensores']  # Nome correto da coleção

    # Documento a ser inserido
    document = {
        "Tipo_dado": "temperatura",
        "Dado": 100
    }

    # Inserção do documento na coleção
    insert_doc = collection.insert_one(document)

    # Exibindo o ID do documento inserido
    print(f"Documento inserido com sucesso! ID: {insert_doc.inserted_id}")

except Exception as e:
    # Tratamento de erros
    print(f"Erro durante a conexão ou operação com o MongoDB: {e}")
finally:
    # Fechando a conexão
    if 'cliente' in locals():
        cliente.close()
        print("Conexão com o MongoDB encerrada.")
