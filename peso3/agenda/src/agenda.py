from contato import Contato
from identificador import Identificador


class Agenda:
    def __init__(self):
        self.contatos = []
        self.quantidade = 0
        self.qntFonesT = 0
        self.qntFones = 0


    def getContatos(self) -> list:
        return self.contatos

    def getQuantidadeDeContatos(self) ->  int:
        return self.quantidade

    def getContato(self, nome:str) -> Contato:
        for name in self.contatos:
            if name == nome:
                return name

    def adicionarContato(self, contato: Contato) -> bool:
        if isinstance(contato, Contato) and contato not in self.contatos:
            self.contatos.append(contato)
            self.quantidade += 1

            return True
        else:
            return False

    def removerContato(self, nome: str) -> bool:
        return False

    def removerFone(self, nome:str, index: int) -> bool:
        return False

    def getQuantidadeDeFones(self, identificador: Identificador) -> int:
        return 0

    def getQuantidadeDeFonesT(self) -> int:
        return self.qntFones

    def pesquisar(self, expressao:str) -> list:
        return None
