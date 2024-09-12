#Método de Busca Leitura
with open("aula-python/text/exemplo_aula05.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#Método de Busca Escrever
with open("aula-python/text/exemplo2_aula05.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá!")
    arquivo.write("Mundo!")
#como não temos um arquivo desse segundo exemplo, ele criará automaticamente

#Método de Acrescentar
with open("aula-python/text/exemplo_aula05.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nTexto Adicionado Exemplo3")