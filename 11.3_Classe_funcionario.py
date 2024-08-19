# Primeira opção #

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def __str__(self):
        return f'\nNome: {self.nome}, CPF: {self.cpf}, Salário: R$ {self.salario:.2f}\n'
    

nome = input("Digite o nome do Funcionario 1: ")
cpf = input("Digite o cpf: ")

Funcionario1 = Funcionario(nome, cpf, 2500)
Funcionario2 = Funcionario("Pedrita da Pedra", "40234559795", 4500)

print (Funcionario1)
print (Funcionario2)

############################################################################



# Segunda opção, simplificado, entrada de dados direto no construtor #
class Funcionario:
    def __init__(self):
        self.nome = input("Digite o nome do funcionário: ")
        self.cpf = input("Digite o CPF do funcionário: ")
        self.salario = float(input("Digite o salário do funcionário: "))

    def __str__(self):
        return f'\nNome: {self.nome}, CPF: {self.cpf}, Salário: R$ {self.salario:.2f}\n'


# Criando as instâncias dos funcionários
Funcionario1 = Funcionario()
Funcionario2 = Funcionario()

# Exibindo as informações dos funcionários
print(Funcionario1)
print(Funcionario2)
