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