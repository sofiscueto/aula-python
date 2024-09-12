#Manipulação de Listas: Crie um programa que inicie com uma lista de frutas. O programa deve permitir que o usuário adicione uma nova fruta à lista e, em seguida, remova uma fruta existente.
# Frutas Iniciais: maça, banana, laranja
# Para esse desafio utilize:
# ● append() função para adicionar item na lista
#       lista.append(novo_item)
# ● remove() função para remover item na lista
#    lista.remove(item_remover)
# ● Utilize if da seguinte maneira
#       if item_remove in lista:
#       Esse if tem o significado de = “Se o item que você quer remover existe na lista = True”

frutas = ['maçã', 'banana', 'laranja']
print(f"Frutas na lista: {frutas}")
novafruta = input("Digite o nome da fruta que você deseja adicionar: ").split().lower()
frutas.append(novafruta)
print(f"Lista atualizada:{frutas}")
# Remover uma fruta existente da lista
retirarfruta = input("Digite o nome da fruta que você deseja remover: ").split().lower()
if retirarfruta in frutas:
    frutas.remove(retirarfruta)
    print(f"Lista atualizada:{frutas}")
else:
    print(f"A fruta '{retirarfruta}' não está na lista.")