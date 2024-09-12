#Manipulação de Dicionários/Objetos: Criar um dicionário que armazene informações sobre um livro (título, autor, ano). O programa deve permitir ao usuário atualizar o ano de publicação e imprimir a informação atualizada..
livro = {"titulo": "A Biblioteca da Meia Noite", "autor": "Matt Haig", "ano": "2021"}
print("Sobre o livro:", livro)
anoAtualizada = input("Digite a nova data: ")
livro["ano"] = anoAtualizada
print(f"Informações sobre o livro atualizadas: {livro}")
