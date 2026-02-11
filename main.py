import json

ENDERECO_TAREFAS = "data/tasks.json"

def carregar_tarefas():
    lista = []
    try:
        with open(ENDERECO_TAREFAS, "r") as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
            pass
    except json.JSONDecodeError:
            pass
    return lista

def salvar_tarefas(lista):
    with open(ENDERECO_TAREFAS, "w") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

def adicionar():
    print("Preencha com as informações: tarefa, grau de urgência."
                    "\n(Lembre-se de separar com vírgula e espaço!)")
    print("")
    entrada = input()
    print("")
    campos = entrada.split(",")

    if len(campos) != 2:
        print("Formatação incorreta!")
        print("")
        return None

    tarefa = []
    tarefa.append(campos[0].strip())
    tarefa.append(False)
    tarefa.append(campos[1].strip())
    print("Tarefa adicionada com sucesso!")
    print("")
    return tarefa

def listar_tarefas(lista):
    for indice, tarefa in enumerate(lista):
        status = "[x]" if tarefa[1] else "[ ]"
        print(f"{indice + 1}) {status} {tarefa[0]}\n   urgência: {tarefa[2]}")

def marcar_concluida(lista):
    status = True
    for i in range(len(lista)):
        if lista[i][1] == False:
            status = False

    if not status:
        while True:
            print("")
            n = int(input("Digite o número da tarefa concluída: "))
            print("")

            if 1 <= n <= len(lista):
                if lista[n-1][1] == False:
                    lista[n-1][1] = True
                    print("Tarefa marcada como concluída!")
                    break
                else:
                    print("Essa tarefa já foi concluída, selecione outra tarefa!")
            else:
                print("Tarefa inexistente.")
    else:
        print("")
        print("Todas as tarefas já estão concluídas!")

def remover_tarefa(lista):
    if len(lista) != 0:
        print("")
        n = int(input("Selecione qual tarefa deseja remover: "))
        print("")
        if 0 < n <= len(lista):
            lista.remove(lista[n - 1])
            print("Tarefa removida com sucesso!")
        else:
            print("Essa tarefa não existe!")
    else:
        print("Sem tarefas por enquanto.")
    return lista

lista_de_tarefas = carregar_tarefas()
print("")
print("⭐ TO-DO LIST ⭐")
print("================")
i = True

while True:
    print("Selecione uma ação:\n1. Adicionar tarefa."\
    "\n2. Listar tarefas."
    "\n3. Marcar tarefa concluída." \
    "\n4. Remover tarefa."
    "\n5. Sair.")
    print("================") if i else None
    i = False
    print("")

    acao = int(input())
    print("")

    if acao == 1:
        nova_tarefa = adicionar()
        if nova_tarefa is not None:
            lista_de_tarefas.append(nova_tarefa)

    elif acao == 2:
        if len(lista_de_tarefas) != 0:
            listar_tarefas(lista_de_tarefas)
        else:
            print("Sem tarefas por enquanto.")
        print("")

    elif acao == 3:
        if len(lista_de_tarefas) == 0:
            print("Sem tarefas por enquanto.")
        else:
            listar_tarefas(lista_de_tarefas)
            marcar_concluida(lista_de_tarefas)
        print("")

    elif acao == 4:
        listar_tarefas(lista_de_tarefas)
        remover_tarefa(lista_de_tarefas)
        print("")
    
    elif acao == 5:
        salvar_tarefas(lista_de_tarefas)
        break

    else:
        print("Digite um número válido!")
        print("")
