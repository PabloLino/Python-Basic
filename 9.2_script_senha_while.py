# criando um script de senha utlizando o while

x = int(input("Digite a senha: "))

while x != 1234:
    print("senha incorreta! ")
    x = int(input("Digite a senha novamente: "))
print("Senha correta, acesso autorizado")