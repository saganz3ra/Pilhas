'''
1. Escreva uma função recursiva em Python que calcule a soma dos primeiros N
números inteiros positivos.
'''

def recursiva(N, pilha=[]):
    if N == 0:
        
        return 0
    else:
        pilha.append(N)
        resultado = recursiva(N - 1, pilha)
        soma = sum(pilha)
        pilha.pop()
        return soma

N = 5  
resultado = recursiva(N)
print(f'A soma dos primeiros {N} números inteiros positivos é {resultado}')