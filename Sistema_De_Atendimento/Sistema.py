from Fila.Fila import Fila
from HeapMaximo.HeapMaximo import HeapMaximo
from Pilha.Pilha import Pilha

class Sistema_de_Atendmento:
    def __init__(self):
        self.fila_comum = Fila()
        self.fila_prioritaria = HeapMaximo()
        self.historico = Pilha()
        
sistema = Sistema_de_Atendmento()
print(sistema.fila_comum.tamanho_da_fila())
print(sistema.fila_prioritaria.tamanho())
print(sistema.historico.tamanho())

