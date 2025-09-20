def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
	contato = {"nome": nome_contato, "telefone": telefone_contato, "email":email_contato, "favorito": False}
	agenda.append(contato)
	print(f"\nO contato de {nome_contato} foi adicionado(a) com sucesso!")
	return

def ver_contatos(agenda):
	print("\nContatos da agenda:")
	print("\n [*] = favorito")
	for indice, contato in enumerate(agenda, start = 1):
		status = "*" if contato["favorito"] else " "
		nome_contato = contato["nome"];
		telefone_contato = contato["telefone"];
		email_contato = contato["email"];
		print(f"{indice}. [{status}] {nome_contato} = Telefone: {telefone_contato}  E-mail: {email_contato}")
	return
