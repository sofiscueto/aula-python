#Atividade1: Crie um programa que imprima os números de 1 a 10 (Utilize for e range).
for i in range(1, 11):
    print(i)
    
#Atividade2: Dada uma lista de frutas, imprima o índice e o nome de cada fruta (Utilize for e enumerate).
frutas = ['Maça', 'Banana', 'Uva', 'Laranja']
for indice, fruta in enumerate(frutas):
    print(f'Índice: {indice}:{fruta}')
    
#Atividade3: Crie um programa que imprima os números pares de 0 a 20. (Utilize for e range)
for i in range(0, 21, 2):
    print("Par: ",i)

#Atividade4: Crie um programa que imprima apenas os números ímpares de 0 a 10. (Utilize for, range e continue)
for i in range(11):
    if i % 2 == 0:
        continue
    print("Ímpar: ",i)

#Atividade5: Crie um programa que solicite ao usuário que insira números até que ele digite 0, e então imprima a soma desses números. (Utilize while)
soma = 0
numero = ""
while numero != 0:
    numero = int(input("Insira um número (quando quiser sair da soma digite 0): "))
    soma += numero
print(f"A soma dos números digitados é igual a: {soma}!")
