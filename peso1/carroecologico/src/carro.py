class Carro:

    def __init__(self):
        self.tank = 0
        self.passageiros = 0
        self.quilometragem = 0



    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.tank

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros == 0 or self.passageiros ==1 :
            self.passageiros += 1
            return True
        else:
            return False

    def desembarcar(self):
        if self.passageiros == 2 or self.passageiros == 1:
            self.passageiros -=1
            return True
        else:
            return False

    def dirigir(self, distancia):

        if self.passageiros > 0 and self.tank > 0:
            if self.tank > distancia:
                self.tank -= distancia
                self.quilometragem += distancia
                return True
            elif self.tank < distancia:
                if self.tank > 100:
                    x = self.tank - 100
                    self.quilometragem += self.tank - x
                    self.tank = 0

                else:
                    self.quilometragem += self.tank
                    self.tank = 0

        else:
            return False
