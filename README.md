# Sistema de Atendimento — Estrutura de Dados

Projeto final da disciplina de **Estrutura de Dados** do curso de Análise e Desenvolvimento de Sistemas (ADS) — 3º Período — IFPE.

Simulação de um sistema de atendimento de clínica médica utilizando estruturas de dados implementadas do zero em Python.

---

## Sobre o Projeto

O sistema gerencia filas de pacientes distinguindo entre pacientes **comuns** e **prioritários**, garantindo que casos de maior urgência sejam atendidos primeiro. Também permite desfazer o último atendimento realizado.

---

## Estruturas de Dados Utilizadas

| Estrutura | Princípio | Uso no sistema |
|---|---|---|
| **Fila** | FIFO — First In, First Out | Pacientes comuns aguardando atendimento |
| **Heap Máximo** | Maior prioridade sempre na raiz | Pacientes prioritários (idosos, gestantes, emergências) |
| **Pilha** | LIFO — Last In, First Out | Histórico de atendimentos — permite desfazer |

Todas as estruturas foram implementadas manualmente, sem uso de bibliotecas prontas.

---

## Estrutura do Projeto

```
Sistema-gerenciamento-atendimento/
│
├── Fila/
│   └── Fila.py
│
├── HeapMaximo/
│   └── HeapMaximo.py
│
├── Pilha/
│   └── Pilha.py
│
└── Sistema.py
```

---

## Como Executar

**Pré-requisito:** Python 3 instalado.

No terminal, na pasta raiz do projeto:

```bash
python Sistema.py
```

---

## Funcionalidades

```
=============================
   SISTEMA DE ATENDIMENTO
=============================
1. Cadastrar paciente comum
2. Cadastrar paciente prioritário
3. Chamar próximo paciente
4. Desfazer último atendimento
5. Ver filas
6. Sair
=============================
```

- **Opção 1** — Cadastra paciente na fila comum
- **Opção 2** — Cadastra paciente prioritário com nível de prioridade:
  - `3` → Idoso
  - `4` → Gestante
  - `5` → Emergência
- **Opção 3** — Chama o próximo paciente (prioritários sempre antes dos comuns)
- **Opção 4** — Desfaz o último atendimento, devolvendo o paciente à fila correta
- **Opção 5** — Exibe todos os pacientes aguardando nas duas filas
- **Opção 6** — Encerra o sistema

---

## Autor
**Jaldson Arthur Silva Portela**  
ADS — 3º Período — IFPE
