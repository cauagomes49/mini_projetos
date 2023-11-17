from funcionario import Funcionario
from irh_service import IRHService
from professor import Professor
from sta import STA
from terceirizado import Terceirizado
from tipo import Tipo




class RHService(IRHService):

    def __init__(self):
        self.funcionarios = []
        self.total = 0
        self.salarios = {'A': 3000,'B': 5000,'C': 7000,'D': 9000,'E': 11000, 't_insalubre': 1500, 'terceirizado': 1000}
        self.salario_sta = 0





    def cadastrar(self, funcionario: Funcionario):
        if isinstance(funcionario, Professor):
            if 'A' <= funcionario.classe <= 'E':
                if funcionario.cpf not in [professor.getCpf() for professor in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True
            return False

        if isinstance(funcionario, STA):
            if 1 <= funcionario.nivel <= 30:
                if funcionario.cpf not in [sta.getCpf() for sta in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True
            return False

        if isinstance(funcionario, Terceirizado):
            if funcionario.cpf not in [terceirizado.getCpf() for terceirizado in self.funcionarios]:
                self.funcionarios.append(funcionario)
                return True
            return False


    def remover(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                self.funcionarios.remove(funcionario)
                return True
        return False

    def obterFuncionario(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
        return None

    def getFuncionarios(self):
        return sorted(self.funcionarios, key=lambda funcionario: funcionario.nome)

    def getFuncionariosPorCategorias(self, tipo):

        if tipo == tipo.STA:
            lista = [funcionario for funcionario in self.funcionarios if isinstance(funcionario, STA)]

        if tipo == tipo.PROF:
            lista = [funcionario for funcionario in self.funcionarios if
                                    isinstance(funcionario, Professor)]
        if tipo == tipo.TERC:
            lista = [funcionario for funcionario in self.funcionarios if
                                    isinstance(funcionario, Terceirizado)]
        lista.sort(key=lambda funcionario: funcionario.nome)
        return lista





    def getTotalFuncionarios(self):
        return len(self.funcionarios)

    def solicitarDiaria(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.obter_diarias() < 3:
                funcionario.adicionar_diaria()
                return True
            return False
        elif isinstance(funcionario, STA):
            if funcionario.obter_diarias() < 1:
                funcionario.adicionar_diaria()
                return True
            return False
        elif isinstance(funcionario, Terceirizado):
            return False

    def partilharLucros(self, valor: float):
        if self.funcionarios:
            self.total = valor / len(self.funcionarios)
            return True

    def iniciarMes(self):
        self.salarios = {'A': 3000, 'B': 5000,'C': 7000,'D': 9000,'E': 11000, 't_insalubre': 1500, 'terceirizado': 1000}
        self.salario_sta = 0
        self.total = 0
        return True

    def calcularSalarioDoFuncionario(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.obter_diarias() > 0:
                salario = self.salarios[funcionario.classe] + (funcionario.obter_diarias() * 100) + self.total
                return salario
            else:
                return self.salarios[funcionario.classe] + self.total

        elif isinstance(funcionario, STA):
            if funcionario.obter_diarias() == 1:
                self.salario_sta = 1000 + (100 * funcionario.nivel) + 100 + self.total
                return self.salario_sta
            else:
                self.salario_sta = 1000 + (100 * funcionario.nivel) + self.total
                return self.salario_sta

        elif isinstance(funcionario, Terceirizado):
            if funcionario.insalubre:
                return self.salarios['t_insalubre'] + self.total
            else:
                return self.salarios['terceirizado'] + self.total


    def calcularFolhaDePagamento(self):
        self.folha_de_pagamento = 0

        if self.funcionarios:
            professores = self.getFuncionariosPorCategorias(Tipo.PROF)
            stas = self.getFuncionariosPorCategorias(Tipo.STA)
            tercs = self.getFuncionariosPorCategorias(Tipo.TERC)

            for professor in professores:
                salario = self.calcularSalarioDoFuncionario(professor.cpf)
                self.folha_de_pagamento += salario

            for sta in stas:
                salario = self.calcularSalarioDoFuncionario(sta.cpf)
                self.folha_de_pagamento += salario

            for terc in tercs:
                salario = self.calcularSalarioDoFuncionario(terc.cpf)
                self.folha_de_pagamento += salario

            self.folha_de_pagamento

            return self.folha_de_pagamento
        return 0