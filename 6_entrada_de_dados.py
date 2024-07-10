# Adicionar uma variável com input e depois exibir o resultado com os dados inseridos
# Quando utilizamos a entrada de dados por meio da função input, essa será considerada do tipo string. Assim, caso seja necessário realizar
# A entrada de valores numéricos, temos de converter o tipo de dado, de acordo com o tipo que desejamos armazenar na variável.

nome = input ("Digite seu nome: ")
cpf = input ("Digite seu CPF: ")
altura = float (input("Digite sua altura: "))
salario = float (input("Digite seu salário: "))
ativo = True

print ("Nome cadastrado com sucesso: %s " % nome)
print ("CPF cadastrado com sucesso: %s" % cpf)
print ("Altura cadastrada com sucesso: %.2f" % altura)
print ("Salário cadastrado com sucesso: %.2f " % salario)
print ("Ativo: %r " % ativo) 





#Sequência de escapes

#Utilizamos a sequência de escapes para auxiliar na formatação da exibição dos dados.
#Para aplicá-los, utilizamos uma combinação de caracteres associados a uma contra barra (\).
#Vamos visualizar as opções:

#Sequência	Descrição
#\n	Insere uma quebra de linha.
#\t	Insere tabulação horizontal.
#\v	Insere tabulação vertical.
#\r	Equivalente ao efeito da tecla Enter.
#\'	Aspas simples.
#\”	Aspas duplas.
#\\	Insere uma barra invertida (backslash).
#\a	Chamado de ASC bell ou beep do sistema. Se houver suporte, aciona um bipe.
#\b	Aciona o backspace, ou seja, apaga o caractere anterior.
#\f	Insere uma quebra de página.
#\u	Insere um caractere UNICODE. Deve acompanhar um código com 4 números.