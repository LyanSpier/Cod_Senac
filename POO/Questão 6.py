#6-Desenvolva uma função sobre parâmetro *argsdef adicao(*args):
resultado = 0    
for argumento in args:
    resultado += argumento
    return resultado
print(adicao(1, 2, 6, 8, 10))
print(adicao(3, 5, 7, 11))
print(adicao(1, 24, 60, 8, 10))