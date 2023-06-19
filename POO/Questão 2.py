
#2-Faça uma funçao que receba uma lista como parâmetro e retorne somente os números pares da lista. 
def lst(): 
     
    lista=[] 
    pares=[] 
     
    n1 = int(input("Digite o primeiro numero: ")) 
    lista.append(n1) 
    n2 = int(input("Digite o segundo numero: ")) 
    lista.append(n2) 
    n3 = int(input("Digite o terceiro numero: ")) 
    lista.append(n3) 
    n4 = int(input("Digite o quarto numero: ")) 
    lista.append(n4) 
     
    for i, num in enumerate(lista): 
        if num % 2==0: 
            pares.append(num) 
    print(pares) 
lst()

