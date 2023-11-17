from contato import Contato
from identificador import Identificador


class Agenda:
    def __init__(self):
        self.contatos = []
        self.fones = []


    def getContatos(self) -> list:
        self.contatos.sort(key=lambda contato: contato.getName())
        return self.contatos

    def getQuantidadeDeContatos(self) ->  int:
        return len(self.contatos)

    def getContato(self, nome:str) -> Contato:

        for contato in self.contatos:
            if contato.getName() == nome:
                return contato

        return None

    def adicionarContato(self, contato: Contato) -> bool:
            if contato.getFones():
                if contato.getName() not in [c.getName() for c in self.contatos]:
                    self.contatos.append(contato)
                    self.fones.extend(contato.getFones())
                    return True
                else:
                    for contatos in self.contatos:
                        if contatos.getName() == contato.getName():
                            contatos.getFones().extend(contato.getFones())
                            self.fones = contatos.getFones()
                            return False

    def removerContato(self, nome: str) -> bool:
        for c in self.contatos:
            if c.nome == nome:
                self.contatos.remove(c)
                return True
        return False


    def removerFone(self, nome:str, index: int) -> bool:
        for contato in self.contatos:
            if contato.nome == nome:
                if 0 <= index < len(
                        contato.fones):
                    contato.fones.pop(index)
                    return True
        return False


    def getQuantidadeDeFonesPorIdentificador(self, identificador: Identificador) -> int:
        count = 0
        for fone in self.fones:
            if fone.identificador == identificador:
                count += 1
        return count

    def getQuantidadeTotalDeFones(self) -> int:
        return len(self.fones)

    def pesquisar(self, expressao:str) -> list:
        self.contatos.sort(key=lambda x: x.getName())
        resultados = []
        for contato in self.contatos:
            if expressao.lower() in contato.getName().lower():
                resultados.append(contato)

            for fone in contato.getFones():
                if expressao.lower() in fone.getIdentificador().name.lower():
                    resultados.append(contato)
                    break

                if expressao in fone.getNumero():
                    resultados.append(contato)
                    break

        return resultados


