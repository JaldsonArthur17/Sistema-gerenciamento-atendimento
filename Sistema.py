#sistema junta as 3 estruturas de dados 
#Fila para pacientes comuns
#HeapMaximo para pacientes prioritários
#Pilha para histórico de atendimentos (permite desfazer)

from Fila.Fila import Fila
from HeapMaximo.HeapMaximo import HeapMaximo
from Pilha.Pilha import Pilha
class Sistema_de_Atendimento:
    def __init__(self):
        self.fila_comum = Fila()#pacientes sem prioridade
        self.fila_prioritaria = HeapMaximo()#pacientes com prioridade
        self.historico = Pilha()#registro de atendimentos

    def cadastrar_paciente(self, nome, prioritario=False, prioridade=1):
        #Opções de caminho para o paciente
        #prioritário - Heap nível de prioridade
        #comum - Fila ordem de chegada
        if prioritario:
            paciente = {"nome": nome, "tipo": "prioritario", "prioridade": prioridade}
            self.fila_prioritaria.adicionar(paciente)
        else:
            paciente = {"nome": nome, "tipo": "comum"}
            self.fila_comum.enfileirar(paciente)

    def chamar_proximo_paciente(self):
        #pacientes prioritários são sempre chamados primeiro

        if not self.fila_prioritaria.esta_vazio():
            #se tiver alguem de prioridade esperando ele remove o de maior prioridade
            paciente = self.fila_prioritaria.remover_max()
        elif not self.fila_comum.esta_vazia():
            #se não houver prioritários ele remove o primeiro da fila comum
            paciente = self.fila_comum.remover_da_fila()
        else:
            #tudo vazio? ninguém para chamar
            print("Nenhum paciente em aguardo")
            return None

        # Todo atendimento realizado é registrado na pilha tendo como desfazer depois
        self.historico.empilhar(paciente)
        print(f"chamando paciente: {paciente['nome']} ({paciente['tipo']})")
        return paciente

    def desfazer_atendimento(self):
        #Pega o atendimento mais recente do histórico 
        paciente = self.historico.desempilhar()

        if paciente is None:
            print("Nenhum atendimento para desfazer.")
            return None

        #envia o paciente para a estrutura correta,
        #baseado tipo que ele tinha no início
        if paciente["tipo"] == "prioritario":
            self.fila_prioritaria.adicionar(paciente)
        else:
            self.fila_comum.enfileirar(paciente)

        print(f"Atendimento desfeito: {paciente['nome']} voltou para a fila.")
        return paciente


#bloco do menu interativo no console

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
            # Cadastro simples que vai pra fila comum
            nome = input("Nome do paciente?: ")
            sistema.cadastrar_paciente(nome)
            print(f"{nome} adicionado à fila comum.")

        elif opcao == "2":
            #Cadastro prioritário que precisa de nível pro heap funcionar
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
            #Desfaz o último atendimento usando o histórico
            sistema.desfazer_atendimento()

        elif opcao == "5":
            #Exibe os pacientes aguardando no geral

            print("\n>>>> Fila Prioritária <<<<<")
            if sistema.fila_prioritaria.esta_vazio():
                print("Nenhum paciente prioritário aguardando.")
            else:
                #lsitar() printa o array do heap
                for p in sistema.fila_prioritaria.listar():
                    print(f"  {p['nome']} (prioridade {p['prioridade']})")

            print("\n>>>>> Fila Comum <<<<<")
            if sistema.fila_comum.esta_vazia():
                print("Nenhum paciente comum aguardando.")
            else:
                #listar_na_fila() retorna por ordem de chegada
                for p in sistema.fila_comum.listar_na_fila():
                    print(f"  {p['nome']}")

        elif opcao == "6":
            print("Encerrando...")
            break

        else:
            print("opção inválida, tente de novo")


#inicialização do menu
menu()