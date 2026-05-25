class Pilha:
    def __init__(self):
        self._dados = []
    
    def empilhar(self, item):
        self._dados.append(item)
    
        