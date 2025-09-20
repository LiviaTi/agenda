from agenda import (
    adicionar_contato,
    ver_tarefas,
    atualizar_nome_tarefa,
    completar_tarefa,
    deletar_tarefas_completadas
)

agenda = []

while True:
    print("\n Minha agenda:")
    print("1. Salvar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Deletar contato")
    print("6. Sair")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome_contato = input("Digite o nome do contato:")
		telefone_contato = input("Digite o telefone do contato:")
		email_contato = input("Digite o email do contato:")
        adicionar_contato(tarefas, nome_contato, telefone_contato, email_contato)
    elif escolha == 2:
        ver_tarefas(tarefas)
    elif escolha == 3:
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da Tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
    elif escolha == 4:
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == 5:
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == 6: