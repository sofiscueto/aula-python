# Calculadora Simples
# Crie uma função para realizar operações matemáticas básicas (adição, subtração, multiplicação, e divisão). A
# função deve receber dois números e a operação desejada como parâmetros e retornar o resultado.
# ● Utilize as boas práticas para nome das funções e das variáveis
# ● Utilize Input para o usuário digitar os dados e lembre de converter o valor do input em float antes de
# utilizar caso necessário!
# ● Retorne uma mensagem “agradável” ao usuário informando sobre o resultado
# ● Utilizar:
#   ○ if operacao not in lista:
# ■ Esse if tem o significado de = “Se operacao não existe na lista = True”
#   ○ if isinstance(resultado, str):
# ■ Método isinstance recebe dois parâmetro ¹ variável para validar com ² tipo de dado

def realizar_operacao(numero1, numero2, operacao):
    # Definindo a lista de operações válidas
    operacoes_validas = ['adição', 'subtração', 'multiplicação', 'divisão']
    
    # Verificar se a operação ta na lista das operações válidas
    if operacao not in operacoes_validas:
        return "Operação inválida. O programa será finalizado."
    
    # Realiza a operação de acordo com a escolha da pessoa
    if operacao == 'adição':
        resultado = numero1 + numero2
    elif operacao == 'subtração':
        resultado = numero1 - numero2
    elif operacao == 'multiplicação':
        resultado = numero1 * numero2
    elif operacao == 'divisão':
        if numero2 == 0:
            return "Erro: Divisão por zero não é permitida."
        resultado = numero1 / numero2
    
    return f"O resultado da {operacao} entre {numero1} e {numero2} é {resultado:.2f}."

def main():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (adição, subtração, multiplicação, divisão): ")
        
        # Chama e exibe o resultado da função
        resultado = realizar_operacao(numero1, numero2, operacao)
        
        # Verifica se o resultado é uma string de mensagem de erro
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"Resultado {numero1} {operacao} {numero2} = {resultado}")
    
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números válidos.")

main()