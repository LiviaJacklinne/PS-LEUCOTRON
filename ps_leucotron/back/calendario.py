# Classe caledário com todos os atributos
class Calendario:
    def __init__(self,id,nome,data,hora,descricao,duracao,local,email):
        self.id = id
        self.nome = nome
        self.data = data
        self.hora = hora
        self.descricao = descricao
        self.duracao = duracao
        self.local = local
        self.email = email
    