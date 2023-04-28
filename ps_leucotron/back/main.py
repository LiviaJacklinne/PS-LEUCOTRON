from database import Database
from calendario import Calendario
from calendarioDAO import CalendarioDAO

# CONEXÃO COM O BANCO
db = Database(database='PS_Leucotron', collection='agenda')
# COMANDO PARA RESETAR O BANCO
# db.resetDatabase()
calendar = CalendarioDAO(db) # INSTANCIANDO UM OBJETO

# VARIAVEL AUXILIAR PARA CRIAR ID UNICO/AUTOMÁTICO
id_compromisso = 0 
flag = True # VARIAVEL AUXILIAR
while(flag): # ESTRUTURA REPETITIVA
    print('1 - Adicionar compromisso')
    print('2 - Editar compromisso')
    print('3 - Ver compromissos')
    print('4 - Deletar compromissos')    
    print('0 - Sair')

    opcao = int(input('O que você deseja fazer: '))

    # CREATE
    if opcao == 1:
        print('------- CRIANDO UM COMPROMISSO ------- ')
        # ENTRADA DE DADOS (INTERFACE AMIGÁVEL)
        nome_compromisso = input('Nome: ')
        data_compromisso = input('Data: ')
        hora_compromisso = input('Hora: ')
        description_compromisso = input('Descrição: ')
        duracao_compromisso = input('Duração: ')
        local = input('Local: ')
        email = input('E-mail: ')
        
        # ATRIBUINDO UM OBJETO
        compromisso = Calendario(id_compromisso, nome_compromisso, data_compromisso, hora_compromisso, description_compromisso, duracao_compromisso, local, email)
        # PASSANDO O OBJETO 
        calendar.createEvento(compromisso)
        id_compromisso +=1

    # UPDATE
    elif opcao == 2:
        print('------- EDITANDO UM COMPROMISSO -------')
        # ENTRADA DE DADOS (INTERFACE AMIGÁVEL)
        id= int(input('ID do compromisso que deseja alterar: '))
        novo_nome = input('Novo Nome: ')
        novo_data = input('Nova Data: ')
        novo_hora = input('Nova Hora: ')
        novo_description = input('Nova Descrição: ')
        novo_duracao = input('Nova Duração: ')
        novo_local = input('Local: ')
        novo_email = input('E-mail: ')
        
        # ATRIBUINDO DIRETO PARA A CLASSE
        calendar.updateEvento(id, novo_nome, novo_data, novo_hora, novo_description, novo_duracao, novo_local, novo_email)
        
    # READ    
    elif opcao == 3:
        print('------- EXIBINDO COMPROMISSOS -------')
        id = input('Digite o ID do compromisso que deseja ver: ')
        calendar.readEvento(id)
        
    # DELETE
    elif opcao == 4:
        print('------- EXCLUIR COMPROMISSO -------')
    
    # SAIR
    elif opcao == 0:
        flag = False
        print('Você saiu!')
    
    # 'DEFAUTL'
    else:
        print('Opção inválida. Tente novamente')