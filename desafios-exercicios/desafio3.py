#Fatiar Strings: Dada uma string com o formato "Primeiro Nome Sobrenome", crie um programa que extraia e imprima apenas o nome do meio (ou seja, o sobrenome)..
# Para esse desafio utilize:
# ● split() é um método de strings que divide a string em uma lista de substrings com base em um delimitador.
#       texto = “Eu me chamo Leonardo”
#       texto.split() # Saída: [‘Eu’, ‘me’, ‘chamo’, ‘Leonardo’]
# ● len() é usada para obter o comprimento (ou número de itens) de um objeto.
#       nome = “Leonardo”
#       len(nome) # Saída: 8"

nome = "Sofia Cueto de Barros"
# Dividindo a string em partes usando o espaço como delimitador
partes = nome.split(" ")
# Verificando se a string contém pelo menos duas partes
if len(partes) > 1:
# O sobrenome está na última posição da lista resultante
    sobrenome = partes[-1]
    print(f"O sobrenome é: {sobrenome}")
else:
    print("A string fornecida não contém um sobrenome.")
