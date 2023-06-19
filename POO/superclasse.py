class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def fazer_barulho(self):
        print("O animal fez barulho!")
            
class Cachorro(Animal):
    def __init__(self,nome,idade,raca):
        super().__init__(nome,idade)
        self.raca = raca 
        
    def aban_rabo(self):
        print("abana o rabo")