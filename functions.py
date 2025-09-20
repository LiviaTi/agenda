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
		nome_contato = contato["nome"]
		telefone_contato = contato["telefone"]
		email_contato = contato["email"]
		print(f"{indice}. [{status}] {nome_contato} = Telefone: {telefone_contato}  E-mail: {email_contato}")
	if (len(agenda) < 1):
		print("Você não possui nenhum contato na sua agenda.")
	return

def editar_contato(agenda, indice_contato, telefone_atualizado):
	indice_contato_int = int(indice_contato) - 1
	if indice_contato_int >= 0 and indice_contato_int < len(agenda):
		agenda[indice_contato_int]["telefone"] = telefone_atualizado
		print(f"Contato {indice_contato} atualizou o número de telefone.")
	else:
		print("Indice de tarefa inválido")
	return

def favoritar_ou_desfavoritar(agenda, indice_contato):
	indice_contato_int = int(indice_contato) - 1
	if indice_contato_int >= 0 and indice_contato_int < len(agenda):
		if (agenda[indice_contato_int]["favorito"] == True):
			agenda[indice_contato_int]["favorito"] = False
		else:
			agenda[indice_contato_int]["favorito"] = True
	else:
		print("Indice de tarefa inválido")
	return

def deletar_contato(agenda, indice_contato):
	indice_contato_int = int(indice_contato) - 1
	if indice_contato_int >= 0 and indice_contato_int < len(agenda):
		agenda.pop(indice_contato_int)
	else:
		print("Indice de tarefa inválido")
	return
