import pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    # CONECTAR DATABASE
    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017" # CONEXÃO LOCAL
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
                
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)
            
    # RESETAR DATABASE
    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            self.collection.insert_many()
            print("Database reseted successfully!")
        except Exception as e:
            print(e)
