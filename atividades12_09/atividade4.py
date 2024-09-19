# Gerenciamento de Contatos com Dicionários/Objetos: Crie um sistema simples para gerenciar uma lista de contatos. Cada contato será representado por um dicionário(objetos) contendo um nome e um número de telefone.
# ● Crie 2 funções sendo:
# ○ Adicionar contato
# ○ Verificar quantidade de contatos
# ● Não utilize Input!
# ○ Adicione os dois contatos na mão!
# ○ Ex:
# ■ {"nome": "Alice", "telefone": "123-456-789"}
# ■ {"nome": "Bob", "telefone": "987-654-321"}
# ● Retorne uma mensagem “agradável” ao usuário informando sobre o resultado


def main():
    contatos = []

    print(f"Sua lista de contatos tem atualmente {len(contatos)}.")

    contato1 = {"nome": "Alice", "telefone": "123-456-789"}
    contato2 = {"nome": "Bob", "telefone": "987-654-321"}

    contatos.append(contato1)
    print(f"Sua lista de contatos tem atualmente {len(contatos)}.")
    print(f"Lista de contatos atualizada: {contatos}")

    contatos.append(contato2)
    print(f"Sua lista de contatos tem atualmente {len(contatos)}.")
    print(f"Lista de contatos atualizada: {contatos}")


main()