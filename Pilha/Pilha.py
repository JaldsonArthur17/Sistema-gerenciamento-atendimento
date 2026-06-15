# Histórico de Atendimentos com princípio LIFO onde o
# último atendimento registrado é o primeiro a ser desfeito.

class Pilha:
    def __init__(self):
        #Lista interna que guarda os atendimentos feitos
        # O final da lista é o topo da pilha
        self._dados = []

    def empilhar(self, item):
        # salva um novo atendimento no topo  da pilha
        # chama sempre que um paciente é chamado no Sistema
        self._dados.append(item)

    def desempilhar(self):
        # Remove e retorna o atendimento do topo
        # pop() sem argumento remove do FINAL da lista
        if len(self._dados) == 0:
            return None
        return self._dados.pop()

    def topo(self):
        # retorna o último atendimento sem remover
        if len(self._dados) == 0:
            return None
        return self._dados[-1]

    def tamanho(self):
        # histórico de atendimentos
        return len(self._dados)