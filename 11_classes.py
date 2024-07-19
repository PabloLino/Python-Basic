#definição de classe simples:
'''
class MinhaNovaClasse:

"Isto é uma docstring. Eu a criei dentro de minha nova classe"

pass
'''


'''
docstring contém uma breve descrição da classe, não é obrigatório, mas é recomendado.
Veja que uma classe cria um namespace, local onde todos os seus atributos são definidos. Os atributos podem ser dados ou funções.
Há também atributos especiais que começam com sublinhados duplos: __.
Por exemplo, __doc__ que nos dá a docstring dessa classe.
'''

class Pessoa:
    """Isto é uma classe nova chamada Pessoa"""
    idade = 15
    
    def saudacao(self):
        print("Olá Pessoas!")

# Output: 15
print(Pessoa.idade)

# Output: <function Pessoa.saudacao at ...>
print(Pessoa.saudacao)

# Output: “Isto é uma classe nova chamada Pessoa”
print(Pessoa.__doc__)
