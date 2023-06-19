#4-Faça uma função que computa a potência ab para valores a e b(assumam números inteiros) passados por parâmetro. 
import math 
def pot(a,b): 
    resp = math.pow(a,b) 
    print(f"o resultado da potência do valor 'a' é {resp}") 
     
pot(5,4)