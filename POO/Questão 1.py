
#1-Faça uma função que peça dois números como parâmetro e mostre na tela o resultado das 4 operações matemáticas. 
 

def operacoes_aritmeticas(n1, n2): 
     
    soma = n1 + n2 
    print("Soma:", soma) 
 

    subtracao = n1 - n2 
    print("Subtração:", subtracao) 
 

    multiplicacao = n1 * n2 
    print("Multiplicação:", multiplicacao) 
 

    if n2 != 0: 
        divisao = n1 / n2 
        print("Divisão:", divisao) 
    else: 
        print("Divisão por zero não é possível.") 
 

numero1 = float(input("Digite o primeiro número: ")) 
numero2 = float(input("Digite o segundo número: ")) 
 
operacoes_aritmeticas(numero1, numero2)

