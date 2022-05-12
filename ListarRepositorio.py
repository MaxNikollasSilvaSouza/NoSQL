import requests
import json 
from salvardb import Repository
import mongoengine

class listaDeRepositorios():

    #passa a URI do banco de dados
    mongoengine.connect( 
        host="mongodb+srv://username:password@servername.5pflo.mongodb.net/databasename?retryWrites=true&w=majority"
    )
    #é a função de inicio do programa, o 'self' é semelhante a um dicionário em python, armazena variáveis na própria classe
    def __init__(self,usuario):
        self._usuario = usuario

    #realiza a requisição
    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code
    
    #imprime a lista de repositórios
    def imprime_repositorios(self):
        dados_api = self.requisicao_api()

        #se a função acima não retornar um erro (Status code), ele entrará nesse IF (ou seja, a variável estará com uma lista)        
        if type(dados_api) is not int:

            #verifico se o usuario quer salvar os repositórios
            print('Para salvar no banco de dados, digite "y", senão digite qualquer outro valor.')
            resposta = input()
            concatena= self._usuario + ';'
            list_repo =[]
           #um laço que será executado até percorrer toda a lista que foi retornada
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
                concatena = concatena + dados_api[i]['name'] + '+'
                if resposta == 'y':        
                    #salvo cada repositório no banco de dados Mongo                       
                    userRepo = Repository(usuario=self._usuario, repositorio=dados_api[i]['name'])
                    userRepo.save()
               # elif resposta == 's':        
                    #salvo cada repositório no banco de dados    
                 #   list_repo.append(dados_api[i]['name'])
                ###preciso fazer uma lista e retornar essa lista pra eu conseguir importar o codigo
            
            if len(list_repo) >2:
                return list_repo
        else:
            print(dados_api)


#self.usuario = usuario
#dados_api = repositorios