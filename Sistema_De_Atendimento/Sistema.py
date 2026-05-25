from Fila.Fila import Fila
from HeapMaximo.HeapMaximo import HeapMaximo
from Pilha.Pilha import Pilha

class Sistema_de_Atendmento:
    def __init__(self):
        self.fila_comum = Fila()
        self.fila_prioritaria = HeapMaximo()
        self.historico = Pilha()
        
    def cadastrar_paciente(self, nome, prioritario = False, prioridade =1):
        if prioritario :
            paciente = {"nome": nome, "tipo": "prioritario", "prioridade": prioridade}
            self.fila_prioritaria.adicionar(paciente)
        else:
            paciente = {"nome": nome, "tipo": "comum"}
            self.fila_comum.enfileirar(paciente)
        
    def chamar_proximo_paciente(self):
        if not self.fila_prioritaria.esta_vazio():
            paciente = self.fila_prioritaria.remover_max()
        elif not self.fila_comum.esta_vazio():
            paciente = self.fila_comum.remover_da_fila()
        else:
            print("Nenhum paciente em aguardo")
            return None
        self.historico.empilhar(paciente)
        print(f"chamando paciente: {paciente['nome']} ({paciente['tipo']})")
        return paciente
            
            
sistema = Sistema_de_Atendmento()
print(sistema.fila_comum.tamanho_da_fila())
print(sistema.fila_prioritaria.tamanho())
print(sistema.historico.tamanho())

sistema.cadastrar_paciente("Ana")
sistema.cadastrar_paciente("Pedro")
sistema.cadastrar_paciente("Gestante", prioritario=True, prioridade=5)
sistema.cadastrar_paciente("Idoso",    prioritario=True, prioridade=4)

print(sistema.fila_comum.listar_na_fila())      
print(sistema.fila_prioritaria.listar()) 

