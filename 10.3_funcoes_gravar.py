# funcao para escrever (write) um doc

arquivo = open('arqv_texto1.txt', 'w')

arquivo.write('Gravando uma mensagem em um arquivo .txt \n')
arquivo.write('Testando')

arquivo.close()

# nesse caso apenas será criado o arquivo com o conteúdo colocado, mas nãio exibirá nenhuma mensagem de confirmação, pois não há um print final
# para isso.

