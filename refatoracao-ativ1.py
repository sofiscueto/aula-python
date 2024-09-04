# Variável dos preços
valores = [100, 200, 300]

# A soma dos 3 valores
totalInicial = sum(valores)
print(f"Total do preço: {totalInicial}") 

desconto = 0
#Aqui ele aplicara um desconto de 10%  caso a compra seja maior que 500, fazendo o calculo do desconto
if totalInicial > 500: 
    desconto = totalInicial * 0.1 
totalDesconto = totalInicial - desconto 

print(f"Desconto aplicado: {desconto}")
print(f"Total com desconto: {totalDesconto}")