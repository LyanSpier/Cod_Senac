class aluno:
    def __init__(self,nome):
        self.nome = nome
        self.notas = []
        
    def adicionar_notas(self,notas):
        self.notas.append(notas)
        
    def calcular_media(self):
        total = sum(self.notas)
        media = total/len(self.notas)
        return media
    
    def verificar_situacao(self):
        media = self.calcular_media()
        
        if media >= 7:
            return "Aprovado!"        
        elif media >= 5 and media < 7:
             return"Recuperação!"
        else:
            return "Reprovação!"