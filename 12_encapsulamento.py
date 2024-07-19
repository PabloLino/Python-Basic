class Televisor_tv:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais= []
        self.volume = 20
    
    def aumentaVolume(self, valor):
        if self.volume+valor <= 100:
             self.volume += valor
        else:
            self.volume=100

    def diminuiVolume(self, valor):
        if self.volume -valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocaCanal(self, canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal

    def sintonizaCanal(self, canal):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)


class Controle_Remoto:
    def __init__(self, tv):
        self.tv = tv

    def aumenta_volume(self):
        self.tv.aumenta_volume(90)

    def diminui_volume(self):
        self.tv.diminui_volume(90)

    def troca_canal(self, canal):
        self.tv.troca_canal(canal)

    def sintoniza_canal(self, canal):
        self.tv.sintoniza_canal(canal)

