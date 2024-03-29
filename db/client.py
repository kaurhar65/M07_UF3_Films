import pymongo

# Conexió a la base de dades
def database():
    try:
        return pymongo.MongoClient("mongodb://localhost:27017").films
    except Exception as e:
        print(f"Ha habido un error: {e}")

#Comprovació per si s'ha connectat o no 
client = database()
if client is not None:
    print("Conexión exitosa a MongoDB.")
else:
    print("No se pudo conectar a MongoDB Atlas. Verifica tus credenciales o la URL de conexión.")