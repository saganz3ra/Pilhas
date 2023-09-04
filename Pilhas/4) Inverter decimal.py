'''
4. Escreva uma função que converte um número decimal em sua representação binária
usando uma pilha.
'''

def decimal(decimal):
    pilha = []
    while decimal > 0:
    
        pilha.append(decimal % 2)
        decimal //= 2
  
    if not pilha:
        return "0"
    binario = ""
    while pilha:
        binario += str(pilha.pop())
    return binario

numero_decimal = int(input("Digite um número decimal: "))
binario = decimal(numero_decimal)
print(f"A representação binária de {numero_decimal} é {binario}")