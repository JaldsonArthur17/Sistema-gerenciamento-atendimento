class Fila:
    def __init__(self):
        self.dados = []
        
    def enfileirar(self, paciente):
        self.dados.append(paciente)
        
        
fila = Fila()
fila.enfileirar("João")
fila.enfileirar("Maria")
print(fila.dados)



