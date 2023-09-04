'''
3. Escreva uma função que use uma pilha para inverter uma string.
'''

def inverter_string_com_pilha():
    string = input("Digite uma palavra para inverter: ")
    pilha = []
    for char in string:
        pilha.append(char)
    string_invertida = ""
    while pilha:
        string_invertida += pilha.pop()
    return string_invertida

string_invertida = inverter_string_com_pilha()
print("Palavra invertida:", string_invertida)