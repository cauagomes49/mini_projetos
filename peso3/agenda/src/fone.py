from identificador import Identificador
import re


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero


    @staticmethod
    def validarNumero(numero) -> bool:
        padrao= r"[\d\(\)\-]*"
        if re.fullmatch(padrao, numero):
            return True
        else:
            return False

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getNumero(self) -> str:
        return self.numero