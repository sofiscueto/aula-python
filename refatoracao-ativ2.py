#Declaração das variáveis
idade = int(input("Digite sua idade: "))

#Analização da categoria de faixa etária do usuário
def validarIdadeUsuario(idade):
    mensagemPadrao = "O usuário é classificado como: "
    if idade < 0:
        return "Essa pessoa por acaso já nasceu?"
    elif idade > 2 and idade <= 2:
        return mensagemPadrao + "Bebê"
    elif idade > 2 and idade < 13:
        return mensagemPadrao + "Criança"
    elif idade >= 13 and idade < 18:
        return mensagemPadrao + "Adolescente"
    elif idade >= 18 and idade < 60:
        return mensagemPadrao + "Adulto"
    elif idade >= 60 and idade <=105:
        return mensagemPadrao + "Idoso"
    else: 
        return "Verifique se o usuário ainda está vivo"

categoriaIdade = validarIdadeUsuario(idade)
#Apresentará o resultado da consulta 
print(categoriaIdade)