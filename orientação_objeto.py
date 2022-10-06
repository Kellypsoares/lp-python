class Aluno: #classe se coloca em letra maiuscula 
        def __init__(self, nome, dre):
                self.nome = nome
                self.dre = dre

        def diga_oi(self):
                return "Oi meu nome eh" + self.nome

a = 