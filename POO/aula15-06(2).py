class Aluno:
    def __init__(self,nome, n1,n2,n3):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        
    #def apresentar(self):
        #print("O aluno ", self.nome)
        
    def verificar(self):
        media = (self.n1+self.n2+self.n3)/3
        if media > 7:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")
            
aluno1 = Aluno