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
        
fila1 = Fila()
fila1.enfileirar({"nome": "Ana"})
fila1.enfileirar({"nome": "Pedro"})
fila1.enfileirar({"nome": "Carlos"})

print(fila1.tamanho_da_fila())
print(fila1.listar_na_fila())

print(fila1.ir_pra_frente())   
print(fila1._dados)  

removido = fila1.remover_da_fila()
print(removido)
print(fila1._dados)




