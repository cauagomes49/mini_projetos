from item import Item
from moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volumeMaximo = volumeMaximo
        self.volume = 0
        self.inteiro = True
        self.itens = ''
        self.moedas = []
    def getVolume(self):
        return self.volume

    def getVolumeMaximo(self):
        return self.volumeMaximo

    def getVolumeRestante(self):
        volume = self.volumeMaximo - self.volume
        return volume

    def addItem(self, item: Item):
        if self.taInteiro() is True:
            if self.getVolumeRestante() >= item.getVolume():
                self.volume += item.getVolume()
                self.itens += f", {item.getDescricao()}"
                self.itens = self.itens[1:]
                return True
            return False


    def add(self, moeda: Moeda):
         if self.taInteiro() is True:
            if self.getVolumeRestante() >= moeda.getVolume():
                self.volume += moeda.getVolume()
                self.moedas.append(moeda.getValor())
                return True
            else:
                return False


    def obterItens(self):
        if self.inteiro is False:
            if self.volume == 0:
                return 'vazio'
            else:
                return self.itens




    def obterMoedas(self):
        if self.inteiro is False:
            soma = sum(self.moedas)
            return soma
        else:
            return -1



    def taInteiro(self):
        return self.inteiro

    def quebrar(self):
        if self.inteiro is True:
            self.inteiro = False
            return True
        else:
            return False