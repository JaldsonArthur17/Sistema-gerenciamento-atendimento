class HeapMaximo:
    def __init__(self):
        self._dados = []
        
    def _pai(self,i):
        return (i-1) // 2
    def _filho_esquerdo(self,i):
        return 2*i + 1
    def _filho_direito(self,i):
        return 2*i + 2
    def _subir(self,i):
        while i > 0:
            pai = self._pai(i)
            if self._dados[i]["prioridade"]>self._dados[pai]["prioridade"]:
                self._dados[i], self._dados[pai] = self._dados[pai], self._dados[i]
                i= pai
            else:
                break
    def adicionar(self,paciente):
        self._dados.append(paciente)
        self._subir(len(self._dados)-1)
        
heap = HeapMaximo()
heap.adicionar({"nome": "Dona Maria", "prioridade": 3})
heap.adicionar({"nome": "Zé",         "prioridade": 1})
heap.adicionar({"nome": "Gestante",   "prioridade": 5})

print(heap._dados)