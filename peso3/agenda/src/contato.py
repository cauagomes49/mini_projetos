from fone import Fone


class Contato:

    def __init__(self, nome):
        self.nome = nome
        self.quantidade = 0
        self.fones = []

    def getName(self) -> str:
        return self.nome

    def getQuantidadeFones(self) -> int:
        return self.quantidade

    def getFones(self) -> list:
        return self.fones

    def adicionarFone(self, fone: Fone) -> bool:
        if fone.validarNumero(fone.numero):
            self.fones.append(fone)
            return True
        else:
            return False

    def removerFone(self, index: int) -> bool:
        if 0 <= index <= len(self.fones):
            self.fones.pop(index)
            return True
        else:
            return False


