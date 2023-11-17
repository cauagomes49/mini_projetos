from exception_base import ExceptionBase


class CirculoNotFoundException (ExceptionBase):


    def __init__(self, ciculoId: str, message="Circulo não encontrado"):
        self.circuloId = ciculoId
        super.__init__(message)

    def getCirculoNaoEncontrado(self):
        return f"Círculo com ID '{self.circuloId}' não foi encontrado."