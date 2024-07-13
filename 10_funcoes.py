'''
def nome_da_funcao (parâmetros):
<intruções>
return "valor do retorno"

def        --> início; 
parêmetros --> podem existir ou não, informações para o processamento da função; 
intruções  --> intruções de entrada, processamento e saída
return     --> quando tiver necessidade de retorno de uma informação
Indentação --> Deve possuir quatro espaços em branco e pular duas linhas para o próximo bloco de instruções (próxima função ou programação principal).
'''

def primeira_mensagem():
    print("Testando função")


def segunda_mensagem():
    return 'Testando com return'


primeira_mensagem()

texto = segunda_mensagem()
print(texto)