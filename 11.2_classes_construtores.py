'''
função __init__().
Esse construtor é chamado sempre que um novo objeto dessa classe é instanciado.
Normalmente é utilizado para inicializar todas as variáveis.
'''

import math

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol = (4 / 3) * math.pi * (self.raio ** 3)
        return vol

    def area(self):
        area = 4 * math.pi * (self.raio ** 2)
        return area

bola1 = Esfera('vermelha', 4)
bola2 = Esfera('azul', 7)

print(f'O volume da bola 1 é {bola1.volume()} cm^3')
print(f'A área superficial da bola 1 é {bola1.area()} cm^2')

print(bola1.volume())
print(Esfera.volume(bola1))
