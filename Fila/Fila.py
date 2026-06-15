
# Pacientes Comuns com princípio FIFO onde o
# primeiro paciente a chegar é o primeiro a ser atendido

class Fila:
    def __init__(self):
        # Lista interna que guarda os pacientes em ordem de chegada
        # O início da lista é a frente da fila
        self._dados = []

    def enfileirar(self, paciente):
        # Adiciona o paciente no final da lista, Quem chega depois vai pro final
        self._dados.append(paciente)

    def remover_da_fila(self):
        # Remove e retorna o paciente da frente da fila e ele vai pro índice 0
        if len(self._dados) == 0:
            return None
        return self._dados.pop(0)

    def ir_pra_frente(self):
        # retorna quem está na frente sem remover
        if len(self._dados) == 0:
            return None
        return self._dados[0]

    def tamanho_da_fila(self):
        # Quantos pacientes estão aguardando 
        return len(self._dados)

    def listar_na_fila(self):
        # Retorna todos os pacientes aguardando por ordem de chegada 
        return self._dados

    def esta_vazia(self):
        # verifica se a fila está vazia
        return len(self._dados) == 0