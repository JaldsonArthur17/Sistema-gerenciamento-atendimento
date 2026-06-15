# Pacientes Prioritários O paciente com MAIOR prioridade está sempre na raiz (índice 0) 
# e é o primeiro a ser atendido.

#  É uma árvore binária representada dentro de um array:
#   índice 0 = raiz
#   filho esquerdo de i = 2*i + 1
#   filho direito de i  = 2*i + 2
#   pai de i = (i-1) // 2

class HeapMaximo:
    def __init__(self):
        # Array que representa a árvore binária do heap
        self._dados = []

    def _pai(self, i):
        # Retorna o índice do pai do nó i
        return (i - 1) // 2

    def _filho_esquerdo(self, i):
        # Retorna o índice do filho esquerdo do nó i
        return 2 * i + 1

    def _filho_direito(self, i):
        # Retorna o índice do filho direito do nó i
        return 2 * i + 2

    def _subir(self, i):
        # Usado após uma inserção
        # O elemento novo entra no final do array e "sobe" na árvore
        # enquanto for maior que o pai
        while i > 0:
            pai = self._pai(i)
            if self._dados[i]["prioridade"] > self._dados[pai]["prioridade"]:
                # Troca o elemento com o pai 
                self._dados[i], self._dados[pai] = self._dados[pai], self._dados[i]
                i = pai
            else:
                #se já estiver no lugar certo ele para o loop
                break

    def adicionar(self, paciente):
        #Coloca o paciente no final do array
        #_subir() para colocá-lo na posição correta
        self._dados.append(paciente)
        self._subir(len(self._dados) - 1)

    def _descer(self, i):
        # Usado após uma remoção da raiz
        # O elemento na posição i "desce" na árvore, trocando de lugar
        # com o filho maior até encontrar seu lugar correto
        n = len(self._dados)
        while True:
            maior = i
            esquerdo = self._filho_esquerdo(i)
            direito = self._filho_direito(i)

            # Verifica se o filho esquerdo existe e é maior
            if esquerdo < n and self._dados[esquerdo]["prioridade"] > self._dados[maior]["prioridade"]:
                maior = esquerdo

            # Verifica se o filho direito existe e é maior
            if direito < n and self._dados[direito]["prioridade"] > self._dados[maior]["prioridade"]:
                maior = direito

            if maior != i:
                # Troca com o filho maior e continua descendo
                self._dados[i], self._dados[maior] = self._dados[maior], self._dados[i]
                i = maior
            else:
                #se já estiver no lugar certo ele para o loop
                break

    def remover_max(self):
        # Remove e retorna o 'maior' paciente na raiz 
        if len(self._dados) == 0:
            return None

        #Troca a raiz com o último elemento do array
        self._dados[0], self._dados[-1] = self._dados[-1], self._dados[0]

        #Remove o que era a raiz
        paciente = self._dados.pop()

        #Reorganiza a árvore a partir da nova raiz
        if len(self._dados) > 0:
            self._descer(0)

        return paciente

    def topo(self):
        # Apenas "olha" o 'maior' paciente, sem remover
        if len(self._dados) == 0:
            return None
        return self._dados[0]

    def tamanho(self):
        # retorna quantos pacientes prioritários estão em aguardo
        return len(self._dados)

    def listar(self):
        # Retorna o array interno para exibição em ordem do array
        return list(self._dados)

    def esta_vazio(self):
        # retorna se ainda existem paciente de prioridade para antes de passar
        # para os comuns
        return len(self._dados) == 0