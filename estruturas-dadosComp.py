#Exemplo de string
texto = "Olá, Mundo!"

#Fatiar do início até um índice específico
print(texto[:5])  #Saída: "Olá, "

#Fatiar de um índicie específico até o final
print(texto[5:])  #Saída: "Mundo!"

#Fatiar do inicio até o final, com um passo específico
print(texto[::2])  #Saída: "Oá ud!"

#Fatiar com início e fim específicos 
print(texto[4:9])  #Saída: " Mund"

#Fatiar com passo negativo para inverter uma substring
print(texto[::-1]) #Saída: "!odnuM  ,álO"


#Exemplo com Lista
frutas = ["maçã", "banana", "laranja"]
print("Lista de frutas:", frutas)

#Adicionando uma fruta
frutas.append("uva")
print("Lista de frutas atualizadas:", frutas)

#Acessando um item 
print("Primeira fruta:", frutas[3])

#Remover alguma fruta da lista
frutas.remove(frutas[2])
print(frutas)


#Exemplo com dicionários/objetos
pessoa = {"nome": "Ana", "Idade": 30}
print("Pessoa:", pessoa)

#Acessando valores
print("Nome:", pessoa["nome"])

#Adicionando um novo par chave-valor
pessoa["cidade"] = "São Paulo"
print("Pessoa aualizada:", pessoa)

#outro teste de dicionários/objetos
pessoa = {"nome": "Benda", "idade": 26, "filhos": {"nome": "Catarina", "idade": 6}}

print(pessoa)

print(pessoa["nome"])

print(pessoa["filhos"])

#print(pessoa["filhos"]["nome"])
pessoaB = pessoa["filhos"]
print(pessoaB["nome"])

del pessoa["filhos"]
print(pessoa)

#ou estre outro teste de dicionários/objetos
listaPessoas = []

pessoa = {"nome": "Ana", "idade": 32}
listaPessoas.append(pessoa)
print(listaPessoas)

pessoa = {"nome": "Benda", "idade": 26}
listaPessoas.append(pessoa)
print(listaPessoas)

pessoa = {"nome": "Fernanda", "idade": 48}
listaPessoas.append(pessoa)
print(listaPessoas)

brenda = listaPessoas[1]
print(brenda)


#Tuplas
# x=10, y=30, z=20
tupla = (10, 30)
print(tupla)
tupla = (tupla[0], 30, tupla[1])
print(tupla)
# x=10, y=30, z=30
tupla = (10, 30, 30)
print(tupla)
novoIndice = 20
tupla = (tupla[0], novoIndice, tupla[2])
print(tupla)


#Conjuntos
#o comando set remove dados repetidos e garante que os elentos sejam únicos
lista = [1, 2, 2, 3, 4, 4]
conjunto = set(lista)
print(conjunto) #saída: {1, 2, 3, 4}

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b) #Interseção: {3}
print(a | b) #União: {1, 2, 3, 4, 5}
print(a - b) #Diferença: {1, 2}

conjunto = {1, 2, 3, 4, 5}
#in = se existe(se tem)
print(3 in conjunto) #saída: True
print(6 in conjunto) #saída: False


#Anotação
variavel: int = "Teste"
print(variavel) #anotação de tipo para uma variável
def soma(a: int, b: int) -> int:
    return a, b 
print(soma("b",3))