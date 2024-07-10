# estrutura condicional para aprovação de período letivo, solicitando o cadastramento de 3 notas, e após fazer a média das notas registradas
# exibe a mensagem de aprovação ou reprovação

#registrando as notas nas variáveis
primeira_nota = float(input("Digite a nota da primeira prova: "))
segunda_nota = float(input("Digite a nota da segunda prova: "))
terceira_nota = float(input("Digite a nota da terceira prova: "))

#cálculo da média das notas registradas
nota_final = (float((primeira_nota + segunda_nota + terceira_nota) / 3))

#verificação
if(nota_final >= 7.0):
    print("Parabéns, você passou de semestre com média: %.1f" %(nota_final))
else:
    print("Você não atingiu a média 7 para ser aprovado, sua nota final ficou: %.1f" %(nota_final))
