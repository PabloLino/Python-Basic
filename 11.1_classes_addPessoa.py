class Pessoa:
    """Isto é uma classe nova chamada Pessoa"""
    idade = 15

    def saudacao(self):
        print('Olá !!!')

# Cria um novo objeto da classe Pessoa
matheus = Pessoa()

# Output: 15
print(matheus.idade)

# Output: <bound method Pessoa.saudacao of <__main__.Pessoa object>>
print(matheus.saudacao)

# Chamando o método saudacao()
# Output: “Olá Pessoas!”
matheus.saudacao()


'''
Em geral, chamar um método com uma lista de n argumentos equivale a chamar a função correspondente com uma lista de argumentos criada 
pela inserção do objeto do método antes do primeiro argumento. Por esses motivos, o primeiro argumento da função na classe deve ser o próprio objeto. 
Isso é convencionalmente chamado self. Ele pode ser nomeado de outra forma, mas é altamente recomendável seguir a convenção.
'''