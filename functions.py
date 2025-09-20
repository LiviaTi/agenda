def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
	contato = {"nome": nome_contato, "telefone": telefone_contato, "email":email_contato, "favorito": False}
	agenda.append(contato)
	print(f"O contato de {nome_contato} foi adicionado(a) com sucesso!")
	return
