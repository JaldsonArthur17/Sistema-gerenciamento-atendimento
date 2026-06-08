class Fila:
    def __init__(self):
        self._dados = []
        
    def enfileirar(self, paciente):
        self._dados.append(paciente)
        
    def remover_da_fila(self):
        if len(self._dados) == 0:
            return None
        return self._dados.pop(0)
        
    def ir_pra_frente(self):
        if len(self._dados) == 0:
            return None
        return self._dados[0]
    
    def tamanho_da_fila(self):
        return len(self._dados)
    
    def listar_na_fila(self):
        return self._dados
    
    def esta_vazia(self):
        return len(self._dados) == 0
        
fila1 = Fila()





