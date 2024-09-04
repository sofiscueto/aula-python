# Variável dos preços
valores = [100, 200, 300]

# A soma dos 3 valores
totalInicial = sum(valores) #soma dos valores

desconto = 0
if totalInicial > 500: #Se o valor total for maior que 500 ele recebera desconto de:
    desconto = totalInicial * 0.1 #Quantidade de desconto que será aplicado

totalDesconto = totalInicial - desconto #Aqui ele vai saber quanto saira com o desconto aplicado caso a compra seja maior que 500

print("Total antes do desconto:", totalInicial)
print("Desconto aplicado:", desconto)
print("Total com desconto:", totalDesconto)