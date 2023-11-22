from grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.grafite = None
        self.folhas = 0

    def inserir(self, grafite: Grafite):
        if self.grafite is None:
            if self.calibre == grafite.calibre:
                self.grafite = grafite
                self.folhas = 0
                return True

    def remover(self):
        if self.grafite is not None:
            self.grafite = None
            return True


    def escrever(self, folhas: int):
        for a in range (0,folhas):
            if self.grafite:
                self.folhas +=1
                self.grafite.tamanho -= self.grafite.desgastePorFolha()
                if self.grafite.tamanho <=0:
                    self.grafite = None
            else:
                return False
        return True


    def getGrafite(self):
        return self.grafite

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhas