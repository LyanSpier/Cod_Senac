class Pessoa:
    def __init__(self, nome, idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def apresentar(self):
        print("Olá meu nome é", self.nome)
        
    def envelhecer(self,anos):
        self.idade += anos 
        #self.idade = self.idade + anos
        print("Minha idade é", self.idade)
        
    def mostracpf(self):
        print("este é o meu cpf:", self.cpf)
        
        
pessoa1 = Pessoa("Raylan", 27, "546.821.673-21")
pessoa2 = Pessoa("Let", 20, "243.512.345-00")
pessoa3 = Pessoa("Sam", 30, "258.987.123-22")

print("---------------------------------------------------------------")
pessoa1.apresentar()
pessoa1.envelhecer(0)
pessoa1.mostracpf()
print("---------------------------------------------------------------")
pessoa2.apresentar()
pessoa2.envelhecer(6)
pessoa2.mostracpf()
print("---------------------------------------------------------------")
pessoa3.apresentar()
pessoa3.envelhecer(2)
pessoa3.mostracpf()