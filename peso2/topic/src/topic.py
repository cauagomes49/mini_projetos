from passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.prioritarios = qtdPrioritarios
        self.normais = capacidade - qtdPrioritarios
        self.AssentosP = []
        self.AssentosN = []


    def getNumeroAssentosPrioritarios(self):
        return self.prioritarios

    def getNumeroAssentosNormais(self):
        return self.normais

    def getPassageiroAssentoNormal(self, lugar):
        if self.AssentosN:
            return self.AssentosN[lugar]



    def getPassageiroAssentoPrioritario(self, lugar):
        if self.AssentosP:
            return self.AssentosP[lugar]



    def getVagas(self):
        vagas = (self.capacidade - len(self.AssentosP) - len(self.AssentosN))
        return vagas


    def subir(self, passageiro: Passageiro):
        cheia = len(self.AssentosP + self.AssentosN)
        if cheia < self.capacidade:
            if passageiro.ePrioridade():
                if len(self.AssentosP) < self.prioritarios:
                    self.AssentosP.append( passageiro)
                    return True
                elif len(self.AssentosN) < self.normais:
                    self.AssentosN.append( passageiro)
                    return True
                else:
                    return False
            else:
                if len(self.AssentosN) < self.normais:
                    self.AssentosN.append( passageiro)
                    return True
                elif len(self.AssentosP) < self.prioritarios:
                    self.AssentosP.append( passageiro)
                    return True
                else:
                    return False
        else:
            return False






    def descer(self, nome):
        for passageiro in self.AssentosN:
            if passageiro.nome == nome:
                self.AssentosN.remove(passageiro)
                return True

        for passageiro in self.AssentosP:
            if passageiro.nome == nome:
                self.AssentosP.remove(passageiro)
                return True

        return False

    def toString(self):
        vazia = self.capacidade - len(self.AssentosP) - len(self.AssentosN)
        if self.capacidade == vazia:
            lista = ' '.join(self.prioritarios * ["@"] + self.normais * ["="])
            return '[' + lista + ' ]'

        resultado1 = ['@'] * self.prioritarios
        resultado2 = ['='] * self.normais

        for i in range(self.prioritarios):
            if i < len(self.AssentosP):
                resultado1[i] = '@' + self.AssentosP[i].getNome()

        for i in range(self.normais):
            if i < len(self.AssentosN):
                resultado2[i] = '=' + self.AssentosN[i].getNome()

        return '[' + ' '.join(resultado1 + resultado2) + ' ]'