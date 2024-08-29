a = 5
b = 3

#igualdade
resultado = a == b
print(resultado)

#Diferença
resultado = a != b
print(resultado)

#Maior que (>)
resultado = a > b
print(resultado)

#Menor que (<)
resultado = a < b
print(resultado)

#Maior ou igual (>=)
resultado = a >= b
print(resultado)

#Menor ou igual (<=)
resultado = a <= b
print(resultado)

#Atividade1- Ana

dia = int(input("Qual o dia de hoje? "))
pedidoPizza = int(input("Quantas pizzas comprou? "))
pedidoBebida = int(input("Quantas bebidas comprou? "))
pedidoBolo = int(input("Quantos bolos comprou? "))
pedidoDoce = int(input("Quantos doces comprou? "))

#Declarando variável
diaFesta = 26
pedidoMinPizza = 10
pedidoMinBebida = 12
pedidoMinBolo = 5
pedidoMinDoce = 600

if diaFesta == dia:
    print("Ana está fazendo as compras no dia da festa!")
else:
    print("Ana está fazendo as compras adiantado!")

if(pedidoMinPizza >= pedidoPizza):
    if(pedidoMinPizza == pedidoPizza):
        print("Ana comprou o minimo permitido de pizza")
    print("Ana não comprou pizzas suficiente!")

if(pedidoMinBebida < pedidoBebida):
    print("Ana comprou mais bebidas que o necessário!")

if(pedidoMinBolo <= pedidoBolo):
    print("Ana excedeu a compra de bolos!")

if(pedidoMinDoce > pedidoDoce):
    print("Ana não comprou doces suficinte!")