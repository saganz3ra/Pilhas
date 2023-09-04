'''
5. Implemente um histórico de comandos de um editor de texto simples usando uma
pilha. A cada vez que um comando é executado, ele é adicionado à pilha.
Implemente a capacidade de desfazer um comando usando a pilha.
'''

class editor:
    def __init__(self):
        self.texto = ""
        self.historico = []

    def adicionar_comando(self, comando):
        self.historico.append(comando)
        self.texto += comando

    def desfazer(self):
        if self.historico:
            comando_desfeito = self.historico.pop()
    
            self.texto = self.texto[:-len(comando_desfeito)]
            return True
        else:
            return False

    def imprimir_texto(self):
        print("Texto atual:", self.texto)

editor = editor()
editor.adicionar_comando("Digitei algo. ")
editor.adicionar_comando("Agora mais texto. ")
editor.imprimir_texto()

if editor.desfazer():
    print("Desfazer realizado.")
else:
    print("Não há comandos para desfazer.")

editor.imprimir_texto()