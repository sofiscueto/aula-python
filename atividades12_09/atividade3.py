# Manipulação de Strings: Crie uma função que receba uma string e retorne a string em maiúsculas, minúsculas e o número de caracteres.
# ● Utilize as boas práticas para nome das funções e das variáveis
# ● Utilize Input para o usuário digitar os dados
# ● Retorne uma mensagem “agradável” ao usuário informando sobre o resultado
# ● Utilize string.upper(), string.lower() e len(string)
# ● Utilize tupla() para retornar os três dados!

def manipular_string():
    entrada_usuario = input("Digite uma string: ")
    
    maiusculas = entrada_usuario.upper()
    minusculas = entrada_usuario.lower()
    numero_caracteres = len(entrada_usuario)

    resultado = (maiusculas, minusculas, numero_caracteres)
    print(f"O resultado da manipulação da sua string é: maiúsculas:{maiusculas}, minúsculas: {minusculas}, número de caracteres da string: {numero_caracteres}.")
    return resultado

manipular_string()