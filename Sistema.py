from Fila.Fila import Fila
from HeapMaximo.HeapMaximo import HeapMaximo
from Pilha.Pilha import Pilha

class Sistema_de_Atendimento:
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
    def desfazer_atendimento(self):
        paciente = self.historico.desempilhar()
        if paciente is None:
            print("Nenhum atendimento para desfazer.")
            return None
        if paciente["tipo"] == "prioritario":
            self.fila_prioritaria.adicionar(paciente)
        else:
            self.fila_comum.enfileirar(paciente)
        print(f"Atendimento desfeito: {paciente['nome']} voltou para a fila.")
        return paciente
            
def menu():
    sistema = Sistema_de_Atendimento()

    while True:
        print("\n=============================")
        print("   SISTEMA DE ATENDIMENTO")
        print("=============================")
        print("1. Cadastrar paciente comum")
        print("2. Cadastrar paciente prioritário")
        print("3. Chamar próximo paciente")
        print("4. Desfazer último atendimento")
        print("5. Ver filas")
        print("6. Sair")
        print("=============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do paciente: ")
            sistema.cadastrar_paciente(nome)
            print(f"{nome} adicionado à fila comum.")

        elif opcao == "2":
            nome = input("Nome do paciente: ")
            print("Nível de prioridade:")
            print("  3 - Idoso")
            print("  4 - Gestante")
            print("  5 - Emergência")
            prioridade = int(input("Prioridade: "))
            sistema.cadastrar_paciente(nome, prioritario=True, prioridade=prioridade)
            print(f"{nome} adicionado à fila prioritária com prioridade {prioridade}.")

        elif opcao == "3":
            pass

        elif opcao == "4":
            pass

        elif opcao == "5":
            pass

        elif opcao == "6":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida.")

menu()