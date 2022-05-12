#importa os dois documentos que estão junto na pasta
import ListarRepositorio as lista


chave = True
#faz um laço infinito
while (chave == True):
    #faz o pedido para o usuário
    print("Digite 1 para listar repositorios ou 2 para sair: ")
    numero = input()
    #tratativa de erro
    try:
        #chama as funções de acordo com o que foi digitado
        int(numero)
        
        #Chama a função de buscar repositórios
        if int(numero) == 1:
            print("Insira o nome do usuário do github: ")
            repositorios = lista.listaDeRepositorios(input())
            repositorios.imprime_repositorios()
        #Chama a função de realizar push
     

        #Encerra o programa
        elif int(numero) == 2:
            chave = False
            exit()
        
        #Avisa o usuário que o valor não é válido
        else:
               print("\nO valor inserido não é válido!")
    
    #Caso haja algum erro, ele será exibido aqui abaixo
    except Exception as e:
        print("\n Causa do" + str(e))
                

