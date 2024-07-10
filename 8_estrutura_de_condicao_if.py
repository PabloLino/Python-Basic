# identação é importante, pois diferente de outras linguagens de programação, no python não há delimitação por chaves ({ })
# condicional if

A = int(input("Digite o valor da variável A: "))
B = int(input("Digite o valor da variável B: "))

if A > B:
    aux = A
    A = B
    B = aux

print("O valor da variável A agora é: ", A)
print("O valor da variável B agora é: ", B)

# nessa estrutura condicional, primeiramente solicita que o usuário dê valores para as variáveis A e B, após isso, o condicional if verifica se 
# o valor de A é maior que B armazenando em uma variavel aux, caso o o valor de B seja menor que A, é alterado os valores das variáveis, como no
# exemplo mostrado.