def adicionar():
    print("Preencha com as informações: tarefa, grau de urgência."
                    "\n(Lembre-se de separar com vírgula e espaço!)")
    entrada = input()
    campos = entrada.split(",")

    if len(campos) != 2:
        print("Formatação incorreta!")
        return None

    tarefa = []
    tarefa.append(campos[0].strip())
    tarefa.append(campos[1].strip())
    
    return tarefa

def listar_tarefas(lista):
    for indice, tarefa in enumerate(lista):
        print(f"{indice + 1}. {tarefa[0]}, (Grau de urgência: {tarefa[1]})")


lista_de_tarefas = []
while True:
    print("Selecione uma ação:\n1. Adicionar tarefa."\
    "\n2. Listar tarefas.")
    acao = int(input())

    if acao == 1:
        nova_tarefa = adicionar()
        if nova_tarefa is not None:
            lista_de_tarefas.append(nova_tarefa)
    elif acao == 2:
        if len(lista_de_tarefas) != 0:
            listar_tarefas(lista_de_tarefas)
        else:
            print("Sem tarefas por enquanto.")
