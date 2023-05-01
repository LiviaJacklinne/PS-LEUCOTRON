from bson.objectid import ObjectId
from database import Database
from calendario import *

# CONECTANDO O BANDO
# db = Database(database='PS_Leucotron', collection='agenda')
# data = db.collection.find()
chave = [] 
class CalendarioDAO(Calendario):
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def createEvento(self, Calendario):
        try:
            result = self.db.collection.insert_one({'ID':Calendario.id,'Nome': Calendario.nome, 'Data': Calendario.data, 'Horário': Calendario.hora, 'Descrição': Calendario.descricao,
                                                    'Duração': Calendario.duracao, 'Local':Calendario.local, 'E-mail ':Calendario.email})
            print(f'Evento criado com id: {result.inserted_id}')
            chave = result.inserted_id
            return result.inserted_id
        except Exception as e:
            print(f'Erro na criação do evento {e}')
            return None
        
    def updateEvento(self, id:int, nome:str, data:str, hora:str, descricao:str, duracao:str,local:str, email:str):
        try:
            result = self.db.collection.update_one({'id': id},{'$set': {'Nome':nome,'Data':data,'Horário': hora, 'Descrição': descricao, 'Duração': duracao,
                                                                        'Local':local, 'E-mail':email}})
            print(f'Evento alterado com sucesso: {result.modified_count}')
            return result.modified_count
        except Exception as e:
            print(f'Erro em alterar o evento: {e}')
            return None
    
    def readEvento(self, id:str):
        try:
            evento = self.db.collection.find_one({'_id':ObjectId(id)})
            print(f'Evento: {evento}') 
            return evento
        except Exception as e:
            print(f'Erro ao ler evento {e}')
            return e
            
        
    def deleteEvento(self, id:int):
        try:
            result = self.db.collection.delete_one({'id': id})
            if result.deleted_count:
                print(f'Evento apagado {id}')
            else:
                print(f'Evento com o id {id} não encontrado')
            return result.deleted_count
        except Exception as e:
            print(f'Erro ao deletar evento: {e}')
            return None