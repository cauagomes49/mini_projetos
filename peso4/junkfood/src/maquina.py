from espiral import Espiral


class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.qtdEspirais = qtdEspirais
        self.maximoProdutos = maximoProdutos
        self.faturamento = 0
        self.saldo = 0
        self.espirais = {indice: Espiral() for indice in range(qtdEspirais)}

    def getFaturamento(self) -> float:
        return self.faturamento

    def getMaximoProdutos(self) -> int:
        return self.maximoProdutos

    def getSaldoCliente(self) -> float:
        return self.saldo

    def getSizeEspirais(self) -> int:
        return self.qtdEspirais

    def getEspiral(self, indice: int) -> Espiral:
        if 0 <= indice < len(self.espirais):
            produto = self.espirais[indice]
            if produto.getQuantidade() == 0:
                self.limparEspiral(indice)
            return produto
        return None




    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.saldo += value
            return True
        return False

    def receberTroco(self) -> float:
        troco = self.saldo
        self.saldo = 0
        return troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        if 0 <= indice < len(self.espirais):
            espiral = self.espirais[indice]
            if quantidade <= self.maximoProdutos:
                espiral.setNomeDoProduto(nome)
                espiral.setQuantidade(quantidade)
                espiral.setPreco(preco)

                return True
        return False

    def limparEspiral(self, indice: int) -> bool:
        if 0 <= indice < len(self.espirais):
            espiral = self.espirais[indice]
            espiral.setNomeDoProduto(" - ")
            espiral.setQuantidade(0)
            espiral.setPreco(0)
            return True
        return False

    def vender(self, indice: int) -> bool:
        if 0 <= indice < len(self.espirais):
            espiral = self.espirais[indice]
            if espiral.getQuantidade() > 0 and espiral.getPreco() <= self.saldo:

                self.faturamento += espiral.getPreco()
                self.saldo -= espiral.getPreco()
                espiral.setQuantidade(espiral.getQuantidade() - 1)
                return True
        return False