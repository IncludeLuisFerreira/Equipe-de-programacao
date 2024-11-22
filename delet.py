from pymongo import MongoClient
MONGO_URI = 'mongodb+srv://prgluis:123@luis.do00k.mongodb.net/?retryWrites=true&w=majority&appName=Luis'

cliente = MongoClient(MONGO_URI)
db = cliente['Extensao']  # Nome correto do banco de dados
collection = db['sensores'] 
for collection_name in db.list_collection_names():
    db[collection_name].delete_many({})  # Remove todos os documentos da coleção
    print(f"Dados da coleção '{collection_name}' deletados.")

print("Todas as coleções foram esvaziadas.")