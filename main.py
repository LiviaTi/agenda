from functions import (
	adicionar_contato,
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
	if escolha == 6:
		break
