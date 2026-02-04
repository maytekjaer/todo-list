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


lista = []
while True:
    print("Selecione uma ação:\n1. Adicionar tarefa.")
    acao = int(input())

    if acao == 1:
        nova_tarefa = adicionar()
        if nova_tarefa is not None:
            lista.append(nova_tarefa)
