# Função para organizar uma lista por tipos
# Função para organizar uma lista por tipos específicos
from enum import Enum

# Definindo a enumeração Tipo
class Tipo(Enum):
    PROF = 'PROF'
    STA = 'STA'
    TER = 'TER'

# Definindo a classe Funcionario
class Funcionario:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

# Classe que contém o método getFuncionariosPorCategorias
class SuaClasse:
    def __init__(self):
        # Suponha que você tenha uma lista de funcionários
        self.funcionarios = [
            Funcionario('Alice', Tipo.PROF),
            Funcionario('Bob', Tipo.STA),
            Funcionario('Carol', Tipo.TER),
            Funcionario('David', Tipo.PROF),
            Funcionario('Eva', Tipo.STA),
            Funcionario('Frank', Tipo.TER),
        ]

    def getFuncionariosPorCategorias(self, tipo: Tipo) -> list:
        """
        Retorna a lista de funcionarios por tipo
        Arguments:
            tipo: tipo de funcionario que devem ser retornados
        Returns:
            lista de funcionario do tipo indicado
        """
        funcionarios_por_tipo = [funcionario for funcionario in self.funcionarios if funcionario.tipo == tipo]
        return funcionarios_por_tipo

