arquivo = open ('teste-testeteste.txt', 'w')

arquivo.write('\nteste ..... auwhsd8uawhd9-awhdf=wa d-a wdfyhua90 -8dfhaw-9 \n')
arquivo.write('final final final\n')
arquivo.write('1010101010011010101010\n')
arquivo.close()

leitura = open ('teste-testeteste.txt', 'r')
print(leitura.read())
leitura.close()

'''

Modos de leitura
Modo	Descrição
r	    Abre o arquivo somente para leitura. O arquivo deve já existir.
r+	    Abre o arquivo para leitura e escrita. O arquivo deve já existir. A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.
w	    Abre o arquivo somente para escrita, no início do arquivo. Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.
w+	    Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente. A	Abre o arquivo para escrita no final do arquivo. Não apaga o conteúdo preexistente.
a+	    Abre o arquivo para escrita no final do arquivo e leitura.

'''
