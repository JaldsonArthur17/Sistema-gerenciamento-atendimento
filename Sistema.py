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
        print("\nSISTEMA DE ATENDIMENTO\n")
        print("1. Cadastrar paciente comum")
        print("2. Cadastrar paciente prioritário")
        print("3. Chamar próximo paciente")
        print("4. Desfazer último atendimento")
        print("5. Ver filas")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do paciente?: ")
            sistema.cadastrar_paciente(nome)
            print(f"{nome} adicionado à fila comum.")

        elif opcao == "2":
            nome = input("Nome do paciente?: ")
            print("Nível de prioridade?:")
            print("  3 --> Idoso")
            print("  4 --> Gestante")
            print("  5 --> Emergência")
            prioridade = int(input("Prioridade: "))
            sistema.cadastrar_paciente(nome, prioritario=True, prioridade=prioridade)
            print(f"{nome} adicionado à fila prioritária com prioridade {prioridade}.")

        elif opcao == "3":
            sistema.chamar_proximo_paciente()

        elif opcao == "4":
            sistema.desfazer_atendimento()

        elif opcao == "5":
            print("\n>>>> Fila Prioritária <<<<<")
            if sistema.fila_prioritaria.esta_vazio():
                print("Nenhum paciente prioritário aguardando.")
            else:
                for p in sistema.fila_prioritaria.listar():
                    print(f"  {p['nome']} (prioridade {p['prioridade']})")

            print("\n>>>>> Fila Comum <<<<<")
            if sistema.fila_comum.esta_vazia():
                print("Nenhum paciente comum aguardando.")
            else:
                for p in sistema.fila_comum.listar_na_fila():
                    print(f"  {p['nome']}")

        elif opcao == "6":
            print("Encerrando...")
            break

        else:
            print("opção inválida, tente de novo")

menu()