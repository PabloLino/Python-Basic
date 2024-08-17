class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def __str__(self):
        return f'\nNome: {self.nome}, CPF: {self.cpf}, Salário: R$ {self.salario:.2f}\n'

Funcionario1 = Funcionario("Pedrão Pedroso", "07720286999", 2500)
Funcionario2 = Funcionario("Pedrita da Pedra", "40234559795", 4500)

print (Funcionario1)
print (Funcionario2)
