# For {referência}
# in {sequência} : {bloco de código}

#for x in range(10):
#    print(x) 

# o código nos retorna os números de 0 a 9, conforme estabelecido no range (10), uma vez que x é menor do que 10 o "print" será executado.
# podemos alterar o valor inicial do laço de repetição, definindo em qual iniciar no range, por exemplo:


for x in range(5, 21):
    print(x)

# nesse caso irá retornar os números de 5 até 20


# podemos também fazer o decremento dos valores, utilizando o -1 no range e invertendo a ordem dos indicadores,
# isso faz que fique em ordem decrescente os valores.
# exemplo:
#for x in range(21, 5, -1):
#    print(x) 