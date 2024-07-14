'''
A função read() realiza a leitura

de todo conteúdo do arquivo.


Sua sintaxe é:

leitura=open('arquivo.txt, 'r')

print leitura.read()

leitura.close()
'''

leitura = open('arqv_texto.txt', 'r')
print (leitura.read())
leitura.close()