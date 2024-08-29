a = 5
b = 3
c = 4

#Adição (+)
resultado = a + b + c 
print(f"Soma: {resultado}")

#Subtração (-)
resultado = c - b
print(f"Subtração: {resultado}")

#Multiplicação (*)
resultado = b * a
print(f"Multiplicação: {resultado}")

#Divisão (/)
resultado = b / a
print(f"Divisão: {resultado}")

#Divisão Inteira (//)
resultado = a // b
print(f"Divisão Inteira: {resultado}")

#Resto da Divisão (%)
resultado = a % b
print(f"Resto da Divisão: {resultado}")

#Exponencial (**)
resultado = a ** b
print(f"Exponencial: {resultado}")

#Atividade José
saldoInicial = 50
custoRefrigerante = 8
custoPao = 4
custoMortadela = 39.90
valorCompra =(custoRefrigerante * 2) + custoPao + ((custoMortadela / 1000) * 300)
saldoFinal = saldoInicial - valorCompra
print(f"José chegou com R${saldoInicial} e saiu com R${saldoFinal}")