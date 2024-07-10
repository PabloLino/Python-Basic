# CONCATENANDO

nome = 'Pedrão da Silva'
idade = 22
cpf = '362.413.950-92'
salario = 2200.50

print ("O nome cadastrado é:",nome, 
       ",a idade da pessoa é:",idade,
       ",Seu cpf cadastrado é:",cpf, 
       "e atualmente está recebendo um salário de:",salario)


# CONCATENANDO COM O SINAL DE +
# Utilizando o sinal de mais devemos converter as variáveis que não são do tipo string para o tipo string, usando o método antes de variável str

nome = 'Pedrito'
idade = 25
cpf = '362.413.950-92'
salario = 3300.50

print ("O nome cadastrado é: " + nome +
       ", a idade da pessoa é: " + str (idade) +
       ", Seu cpf cadastrado é: " + cpf +
       " e atualmente está recebendo um salário de: "+ str (salario)+" Reais")
 