from src.pessoa import Pessoa


class Motoca:

    def __init__(self, potencia=0):
        self.potencia = potencia
        self.pessoa = None
        self.tempo = 0

    def getPessoa(self):
        return self.pessoa


    def getTempo(self):
        return self.tempo

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoa == None:
           self.pessoa = pessoa
           return  True
        else:
            return False


    def descer(self):
        if self.pessoa != None:
            self.pessoa = None
            return True
        else:
            return False




    def colocarTempo(self, tempo: int):
        if tempo > 0:
            self.tempo = tempo
            return True
        else:
            return False

    def dirigir(self, tempo: int):

        if self.pessoa != None and self.tempo != 0:
            if self.pessoa.getIdade() <= 10:
                if self.tempo > tempo:
                    dife = self.tempo - tempo
                    self.tempo = dife
                    return True
                elif tempo > self.tempo:
                    self.tempo = 0
                    return True
            else:
                return False

    def buzinar(self):
          tex = 'Pe'
          if self.pessoa == None :
              return ''
          elif self.pessoa != None:
              for e in tex:
                  if e == 'e':
                      tex += 'e' * (self.potencia -1) + 'm'
                      return tex









