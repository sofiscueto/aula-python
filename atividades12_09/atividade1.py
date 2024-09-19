# Conversão de Temperatura: Crie duas funções: uma para converter Celsius para Fahrenheit e outra para converter Fahrenheit para Celsius.
# As funções devem receber a temperatura como parâmetro e retornar o valor convertido.
#● Utilize as boas práticas para nome das funções e das variáveis
# ● Utilize Input para o usuário digitar os dados e lembre de converter o valor do input em float antes de utilizar
# ● Retorne uma mensagem “agradável” ao usuário informando sobre a conversão
# ● Dica: Ao declarar a variável float no print e utilizar :.2f ele irá arredondar para 2 casas decimais.
#   ○ Ex: print(f”{temperatura_celsius:.2f}°C”) # temperatura_celsius = 38 | Saída: 38.00°C.

def celsius_para_fahrenheit(celsius):
    """Converte a temperatura de Celsius para Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    """Converte a temperatura de Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"A temperatura de {temperatura_celsius:.2f}°C equivale a {temperatura_fahrenheit:.2f}°F.")

temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(f"A temperatura de {temperatura_fahrenheit:.2f}°F equivale a {temperatura_celsius:.2f}°C.")