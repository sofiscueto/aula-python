#Usuario vai informar a idade
idade = int(input("Digite sua idade: "))

#Aqui são definidas as classificações da faixa etária
categoria = "Indefinida"
if idade < 13:
    categoria = "Criança"
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"
elif idade >= 18 and idade < 60:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"

#Apresentará o resultado da consulta 
print(f"O usuário é classificado como {categoria}")