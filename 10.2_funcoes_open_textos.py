'''
função open tem como objetivo abrir um arquivo de texto para a manipulação dos dados na linguagem python.
 A função open() é utilizada para a abertura dos arquivos.
 sintaxe -->     arquivo = open('arquivo.txt', 'w')
 podemos perceber que possui dois parâmetros, o nome do arquivo e o modo que ele será aberto.
'''

# Ao utilizar ‘w’ em um arquivo já existente, ele reescreverá todo o conteúdo do arquivo,
# fazendo com que todos os dados que estavam nele sejam apagados.

# Abre o arquivo em modo de escrita ('w') usando 'with'
# Usar o with dessa maneira é mais seguro e evita problemas caso algo dê errado durante a escrita no arquivo.





with open('novo_exemplo.txt', 'w') as arquivo:
    # Escreve no arquivo
    arquivo.write('Este é um novo exemplo de escrita em arquivos em Python, aqui criamos um novo doc e colocamos as informações desejadas nele.\n')
    arquivo.write('Podemos adicionar várias linhas também, conforme a necessidade.\n')

print('Arquivo escrito com sucesso!')







'''
arquivo.close()

Um dos motivos da necessidade da função close() é que se tentarmos escrever em um arquivo e não o fecharmos depois de terminar a escrita, 
as informações não chegarão ao arquivo e nada será escrito.
'''