#Trabalhar com Tuplas: Criar uma tupla contendo três coordenadas (x, y, z). O programa deve permitir ao usuário alterar a coordenada y e exibir a tupla atualizada.

coordenadas = (10, 20, 30)
print(f"Coordenadas atuais: {coordenadas}")
novo = float(input("Digite o novo valor para a coordenada y: "))
coordenadasAtualizadas = (coordenadas[0], novo, coordenadas[2])
print(f"Coordenadas atualizadas: {coordenadasAtualizadas}")



