def ler_notas():
    n1 = float(input("digite a primeira nota do aluno(a): "))
    n2 = float(input("digite a segunda nota do aluno(a): "))
    return n1,n2


def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("\nNota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: %.1f" %(media), "\nResultado: ", end="")
    if media >= 7.0:
        print("Aprovado\n")
    else:
        print("Reprovado\n")


n1,n2 = ler_notas()
resultado(n1,n2)