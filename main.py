import json

ENDERECO_TAREFAS = "data/tasks.json"

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
    tarefa.append(False)
    tarefa.append(campos[1].strip())
    return tarefa

def listar_tarefas(lista):
    for indice, tarefa in enumerate(lista):
        if tarefa[1] == False:
            tarefa[1] = "Pendente"
        else:
            tarefa[1] = "Concluída"
        print(f"{indice + 1}. {tarefa[0]} - Status: {tarefa[1]} - (Grau de urgência: {tarefa[2]})")

def marcar_concluida(lista):
    n = int(input("Digite o número da tarefa concluída: "))
    
    if 1 <= n <= len(lista):
        lista[n-1][1] = "Concluída"
        print("Tarefa marcada como concluída!")
    else:
        print("Tarefa inexistente.")

def carregar_tarefas():
    lista = []
    try:
        with open(ENDERECO_TAREFAS, "r") as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
        pass
    return lista

def salvar_tarefas(lista):
    with open(ENDERECO_TAREFAS, "w") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

lista_de_tarefas = carregar_tarefas()

while True:
    print("Selecione uma ação:\n1. Adicionar tarefa."\
    "\n2. Listar tarefas."
    "\n3. Marcar tarefa concluída." \
    "\n4. Sair.")

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

    elif acao == 3:
        if len(lista_de_tarefas) == 0:
            print("Sem tarefas por enquanto.")
        else:
            listar_tarefas(lista_de_tarefas)
            marcar_concluida(lista_de_tarefas)

    elif acao == 4:
        salvar_tarefas(lista_de_tarefas)
        break
            
    else:
        print("Digite um número válido!")
