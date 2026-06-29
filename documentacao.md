# Documentação — Sistema de Atendimento

Autor: Jaldson Arthur Silva Portela
Curso: Análise e Desenvolvimento de Sistemas — 3º Período — IFPE
Disciplina: Estrutura de Dados


## O que o projeto faz

O projeto simula um sistema de atendimento de clínica médica. Ele gerencia duas filas de pacientes: uma para pacientes comuns e outra para pacientes prioritários. O sistema garante que pacientes prioritários sejam sempre atendidos antes dos comuns, independentemente da ordem de chegada. Também é possível desfazer o último atendimento realizado, devolvendo o paciente à fila correta.


## O problema que resolve

Sistemas de atendimento tradicionais tratam todos os pacientes da mesma forma, respeitando apenas a ordem de chegada. Isso é ineficiente em situações reais, onde idosos, gestantes e casos de emergência precisam de atendimento urgente, independentemente de quando chegaram. Além disso, não há mecanismo para corrigir erros de chamada. Este sistema resolve os dois problemas: prioridade automática e possibilidade de desfazer atendimentos.


## Estrutura de pastas

    Fila/
        Fila.py
    HeapMaximo/
        HeapMaximo.py
    Pilha/
        Pilha.py
    Sistema.py


## Como executar

Ter o Python 3 instalado. No terminal, dentro da pasta raiz do projeto, executar:

    python Sistema.py

O menu será exibido no terminal com as seguintes opções:

    1. Cadastrar paciente comum
    2. Cadastrar paciente prioritário
    3. Chamar próximo paciente
    4. Desfazer último atendimento
    5. Ver filas
    6. Sair


## Estruturas de dados utilizadas

### Fila

Arquivo: Fila/Fila.py

Princípio: FIFO (First In, First Out). O primeiro paciente a entrar é o primeiro a sair.

Usada para armazenar pacientes comuns em ordem de chegada. Internamente utiliza uma lista, onde novos pacientes são adicionados no final com append() e removidos do início com pop(0), garantindo o comportamento de fila.

Métodos:

- enfileirar(paciente): adiciona o paciente no final da fila
- remover_da_fila(): remove e retorna o primeiro da fila
- ir_pra_frente(): retorna o primeiro sem remover
- tamanho_da_fila(): retorna quantos pacientes estão na fila
- listar_na_fila(): retorna todos os pacientes aguardando
- esta_vazia(): retorna True se a fila estiver vazia


### Heap Máximo

Arquivo: HeapMaximo/HeapMaximo.py

Princípio: o elemento de maior prioridade está sempre na raiz e é o primeiro a ser removido.

Usada para armazenar pacientes prioritários. Internamente representa uma árvore binária dentro de uma lista. A posição de cada elemento é calculada matematicamente: o filho esquerdo do índice i está em 2*i+1, o filho direito em 2*i+2, e o pai em (i-1)//2. Essa relação permite navegar pela árvore sem usar ponteiros.

Toda vez que um paciente é inserido, ele vai para o final da lista e "sobe" comparando com o pai até encontrar sua posição correta (método _subir). Quando o paciente de maior prioridade é removido, o último elemento da lista vai para o topo e "desce" comparando com os filhos até encontrar sua posição correta (método _descer).

Métodos:

- adicionar(paciente): insere o paciente e reorganiza o heap com _subir
- remover_max(): remove e retorna o de maior prioridade, reorganiza com _descer
- topo(): retorna o de maior prioridade sem remover
- tamanho(): retorna quantos pacientes estão no heap
- listar(): retorna o array interno para exibição
- esta_vazio(): retorna True se o heap estiver vazio


### Pilha

Arquivo: Pilha/Pilha.py

Princípio: LIFO (Last In, First Out). O último atendimento registrado é o primeiro a ser desfeito.

Usada para armazenar o histórico de atendimentos realizados. Cada vez que um paciente é chamado, ele é empilhado. Ao desfazer, o sistema desempilha o atendimento mais recente e devolve o paciente à fila de origem.

Métodos:

- empilhar(item): registra o atendimento no topo da pilha
- desempilhar(): remove e retorna o atendimento mais recente
- topo(): retorna o atendimento mais recente sem remover
- tamanho(): retorna quantos atendimentos estão registrados


## A classe principal

Arquivo: Sistema.py

A classe Sistema_de_Atendimento não reimplementa nenhuma estrutura. Ela instancia as três e define as regras de uso.

O método cadastrar_paciente recebe o nome do paciente e decide para qual estrutura ele vai: prioritários entram no Heap com um nível de prioridade, comuns entram na Fila.

O método chamar_proximo_paciente sempre verifica primeiro se há alguém no Heap. Se houver, chama o de maior prioridade. Se o Heap estiver vazio, chama o primeiro da Fila. Se as duas estruturas estiverem vazias, avisa que não há pacientes aguardando. O paciente chamado é sempre empilhado no histórico.

O método desfazer_atendimento desempilha o último atendimento e verifica o campo "tipo" do paciente. Se era prioritário, devolve ao Heap. Se era comum, devolve à Fila.


## Fluxo de execução

1. O usuário inicia o programa e o menu é exibido.
2. Ao cadastrar um paciente, ele é direcionado para a estrutura correta.
3. Ao chamar o próximo, o sistema aplica a regra de prioridade automaticamente.
4. Cada atendimento realizado é registrado na pilha de histórico.
5. Se necessário, o último atendimento pode ser desfeito, devolvendo o paciente à fila original.
6. O ciclo continua até o usuário encerrar o sistema.
