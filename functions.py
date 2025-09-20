def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email":email_contato, "favorito": False}
    agenda.append(tarefa)
    print(f"O contato de {nome_contato} foi adicionado(a) com sucesso!")

def ver_tarefas(tarefas):
    print("\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido")

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_int = int(indice_tarefa) - 1
    if 0 <= indice_tarefa_int < len(tarefas):
        tarefas[indice_tarefa_int]["completada"] = True
        print(f"Tarefa {indice_tarefa} marcada como completada")
    else:
        print("Indice de tarefa inválido")

def deletar_tarefas_completadas(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    print("\nTarefas completadas foram deletadas")
