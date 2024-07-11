'''
qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while 0.0 < valor <= 10:
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um novo valor: "))

# caso o valor digitado esteja fora do intervalo entre 0 até 10 estabelecido na condição do while, irá calcular a média dos valores digitados
# anteriormente a soma dos valores e a quantidade de valores cadastrados

media = soma / qtd

print("\nQuantidade de valores cadastrados: ", qtd)
print("\nSoma dos valores cadastrados: ", soma)
print("\nMédia dos valores: ", media)
'''

# se caso o usuário digite o primeiro valor e não entre nos parâmetros de while, irá retornar um erro, pois o código tenta fazer uma divisão por zero.
# nesse caso podemos colocar um if para que não ocorra esse problema, juntamente com isso, podemos adicionar uma estrutura de lista para armazenar
# os valores que o cliente cadastrou para no final ser exibido com os cálculos, segue o exemplo:


qtd = 0
soma = 0.0
media = 0.0
valores = []  # Lista para armazenar os valores válidos
valor = float(input("Digite um valor: "))

while 0.0 < valor <= 10.0:
    valores.append(valor)  # Adiciona o valor à lista
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um novo valor: "))

# Calcula a média apenas se a quantidade de valores for maior que zero
if qtd > 0:
    media = soma / qtd
    print("\nValores cadastrados:", valores)
    print("\nQuantidade de valores cadastrados:", qtd)
    print("\nSoma dos valores cadastrados:", soma)
    print("\nMédia dos valores:", media)
else:
    print("\nNenhum valor válido foi digitado.\n")
