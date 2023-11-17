from abc import ABC, abstractmethod


class CirculoBase(ABC):

    def __init__(self, id: str, limite: int):
        self.id = id
        self.limite = limite
        self.number = 0

    @abstractmethod
    def setLimite(self, limite: int):
        self.limite = limite

    def getId(self):
        return self.id

    def getLimite(self):
        return self.limite
    @abstractmethod
    def getNumberOfContacts(self):
        return self.number