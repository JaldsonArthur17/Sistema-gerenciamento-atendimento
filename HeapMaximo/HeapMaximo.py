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
        
    def _descer(self,i):
        n =len(self._dados)
        while True:
            maior = i
            esquerdo = self._filho_esquerdo(i)
            direito =self._filho_direito(i)
            
            if esquerdo < n and self._dados[esquerdo]["prioridade"] > self._dados[maior]["prioridade"]:
                maior = esquerdo
            if direito < n and self._dados[direito]["prioridade"]> self._dados[maior]["prioridade"]:
                maior = direito
            if maior != i:
                self._dados[i], self._dados[maior] = self._dados[maior], self._dados[i]
                i = maior
            else:
                break
        
    def remover_max(self):
        if len(self._dados) == 0:
            return None
        
        self._dados[0], self._dados[-1] = self._dados[-1], self._dados[0]
        paciente = self._dados.pop()
        
        if len(self._dados) > 0:
            self._descer(0)
        return paciente
    
    def topo(self):
        if len(self._dados) == 0:
            return None
        return self._dados[0]

    def tamanho(self):
        return len(self._dados)
    
    def listar(self):
        return list(self._dados)
    
    def esta_vazio(self):
        return len(self._dados) == 0
        
heap = HeapMaximo()
