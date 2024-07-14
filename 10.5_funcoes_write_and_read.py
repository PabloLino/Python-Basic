# Abre o arquivo em modo de escrita ('w') e escreve informações nele
with open('write-and-read.txt', 'w') as arquivo:
    arquivo.write("\nCriando arquivo e colocando informações dentro dele\n")
    arquivo.write("Mais infos.......\n")
    arquivo.write("FINAL\n")

print("Documento criado com sucesso!!!")

# Abre o arquivo em modo de leitura ('r') e lê seu conteúdo
with open('write-and-read.txt', 'r') as leitura:
    conteudo = leitura.read()
    print(conteudo)

print("Documento fechado com sucesso!!!")
