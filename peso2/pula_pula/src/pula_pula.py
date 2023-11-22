from crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limite = limiteMax
        self.FilaDeEspera = []
        self.caixa = 0
        self.criancasPulando = []
        self.conta = 0

    def getFilaDeEspera(self):
        return self.FilaDeEspera

    def getCriancasPulando(self):
        return self.criancasPulando


    def getLimiteMax(self):
        return self.limite

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for kid in self.criancasPulando:
            if kid.nome == nome:
                return self.conta


    def entrarNaFila(self, crianca: Crianca):
        if crianca.getName() not in [kid.getName() for kid in self.FilaDeEspera]:
            self.FilaDeEspera.append(crianca)
            return True
        else:
            return False


    def entrar(self):
        if self.FilaDeEspera:
            if len(self.criancasPulando) < self.limite:
                primeiro = self.FilaDeEspera[0]
                self.criancasPulando.append(primeiro)
                self.FilaDeEspera.pop(0)
                self.conta += 2.50
                return True






    def sair(self):
        if self.criancasPulando:
            crianca = self.criancasPulando[0]
            self.criancasPulando.pop(0)
            self.FilaDeEspera.append(crianca)
            return True

    def papaiChegou(self, nome):
        for kid in self.FilaDeEspera:
            if kid.nome == nome:
                self.FilaDeEspera.remove(kid)
                self.caixa += self.conta
                return True

        for kid in self.criancasPulando:
            if kid.nome == nome:
                self.criancasPulando.remove(kid)
                self.caixa += self.conta
                return True

    def fechar(self):
        self.FilaDeEspera.clear()

        for kid in self.criancasPulando:
            self.conta += 2.5
            self.criancasPulando.clear()
            return True





        print(len(self.FilaDeEspera))
