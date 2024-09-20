frutas = ['Maça', 'Banana', 'Uva', 'Laranja']

for fruta in frutas:
    print('A fruta atual é: ', fruta)


    for i in range(6):
        print(i)


for i in range(1, 11, 3):
    print(i)

for indice, valor in enumerate(frutas):
    print(f'Índice: {indice}, Valor: {valor}')



for i in range(23):
    if i % 2 == 0:
        continue
    print('Ímpar: ',i)