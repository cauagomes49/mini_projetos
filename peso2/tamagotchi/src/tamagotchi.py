class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energia = energiaMax
        self.saciedade = saciedadeMax
        self.limpeza = limpezaMax
        self.idade = 0
        self.diamantes = 0


    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energia

    def getSaciedadeAtual(self):
        return self.saciedade

    def getLimpezaAtual(self):
        return self.limpeza

    def getIdadeAtual(self):
        return self.idade

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
            if self.energia > 0 and self.limpeza > 0 and self.saciedade > 0 and self.idade < self.idadeMax:
                return True
            elif self.limpeza < 0:
                self.limpeza = 0
            elif self.energia < 0:
                self.energia = 0
            else:
                return False



    def brincar(self):
        if self.getEstaVivo():
            self.energia -= 2
            self.saciedade -= 1
            self.limpeza = max(self.limpeza -3,0)
            self.diamantes += 1
            self.idade = min(self.idade + 1 ,self.idadeMax)
            return True
        else:
            return False

    def comer(self):
        if self.getEstaVivo():
            self.energia -= 1
            self.saciedade = min(self.saciedade + 4, self.saciedadeMax)
            self.limpeza = max(self.limpeza -2 ,0)
            self.diamantes += 0
            self.idade = min(self.idade + 1 ,self.idadeMax)
            return True




    def dormir(self):
        if self.getEstaVivo():
            if self.energia  <= self.energiaMax - 5:
                turno = self.energiaMax - self.energia
                self.idade += turno
                self.energia = self.energiaMax
                self.saciedade -= 2
                self.limpeza = self.limpeza

                return True
        else:
            return False

    def banhar(self):
        if self.getEstaVivo():
            self.energia -= 3
            self.saciedade -=1
            self.limpeza = self.limpezaMax
            self.diamantes += 0
            self.idade = min(self.idade + 2 ,self.idadeMax)
            return True


        else:
            return False