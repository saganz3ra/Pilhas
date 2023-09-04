'''
2. Escreva uma função recursiva para calcular o número fatorial de um número inteiro
positivo.
'''

def recursivaFatorial(N, pilha=[]):
    if N == 0:
        return 1
    else:
        pilha.append(N)
        resultado = recursivaFatorial(N - 1, pilha)
        fatorial = 1
        for valor in pilha:
            fatorial *= valor
        pilha.pop()
        return fatorial

N = 5 
resultado = recursivaFatorial(N)
print(f'O fatorial de {N} é {resultado}')