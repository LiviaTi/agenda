from functions import (
	adicionar_contato,
	ver_contatos,
	editar_contato,
	favoritar_ou_desfavoritar,
	deletar_contato
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
		nome_contato = input("Digite o nome do contato: ")
		telefone_contato = input("Digite o telefone: ")
		email_contato = input("Digite o email: ")
		adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)
	if escolha == 2:
		ver_contatos(agenda)
	if escolha == 3:
		ver_contatos(agenda)
		indice_contato = input("Digite o indice do contato:")
		telefone_atualizado = input("Digite o novo numero de telefone:")
		editar_contato(agenda, indice_contato, telefone_atualizado)
	if escolha == 4:
		indice_contato = input("Digite o número indice do contato que deseja favoritar ou desfavoritar: ")
		favoritar_ou_desfavoritar(agenda, indice_contato)
	if escolha == 5:
		indice_contato = input("Digite o indice do contato que deseja apagar:")
		deletar_contato(agenda,indice_contato)
	if escolha == 6:
		break
