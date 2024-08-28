print("Olá Mundo!")

numero1 = 1
numero2 = 5
# soma = numero1 + numero2
# print(f"A soma de {numero1} + {numero2} é {soma}")

def teste():
    print("Teste")
teste()

def somar (x, y):
    if x == y:
        return "X é igual a Y"
    return x + y
print(f"A soma é: {somar(numero1, numero2)}")

def subtracao(a, b):
    return a - b
print("A subtração é: {numero1}", subtracao(8,4))

