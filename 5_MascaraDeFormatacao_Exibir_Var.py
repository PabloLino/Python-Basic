"""
Máscara     Tipo de Dado        Descrição
%d ou %i	Int (inteiro)	    Exibe um valor inteiro.
%f	        Float ou double	    Exibe um valor decimal.
%ld	        Long Int	        Exibe um número inteiro longo.
%e ou %E	Float e double	    Exibe um número exponencial (número científico).
%c	        Char (caractere)	Exibe um caractere.
%o	        Int	                Exibe um número inteiro em formato octal.
%x ou %X	Int	                Exibe um número inteiro no formato hexadecimal.
%s	        Char	            Exibe uma cadeia de caracteres (string).
%r	        Boolean	            Exibe true ou false (verdadeiro ou falso).
"""

codigo = 220
name = 'Florisvaldo da Silva'
idade = 48
salario = 2850.80
ativo = True

print ("Código: %d "% codigo)
print ("Nome: %s "% name)
print ("Código: %i "% idade)
print ("Código: %.2f "% salario)
print ("Código: %r "% ativo)

#se colocarmos o tipo de mascara em salario como double, utilizando o recurso %e ou %E, vamos obter um resultado um pouco diferente na saída.
# exemplo: print ("Código: %e "% salario)

print ("Código: %e "% salario)

