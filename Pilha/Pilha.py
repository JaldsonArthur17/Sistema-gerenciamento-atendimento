class Pilha:
    def __init__(self):
        self._dados = []
    
    def empilhar(self, item):
        self._dados.append(item)
        
    def desempilhar(self):
        if len(self._dados) == 0:
            return None
        return self._dados.pop()
    
    def topo(self):
        if len(self._dados) == 0:
            return None
        return self._dados[-1]
    
    def tamanho(self):
        return len(self._dados)
    
pilha = Pilha()
pilha.empilhar({"nome": "Ana",   "hora": "09:00"})
pilha.empilhar({"nome": "Pedro", "hora": "09:15"})
pilha.empilhar({"nome": "Maria", "hora": "09:30"})

print(pilha.desempilhar())
print(pilha.desempilhar())
print(pilha._dados)
print(pilha.topo())
print(pilha.tamanho())

print(pilha._dados)