#Manipulação de Dicionários/Objetos: Criar um dicionário onde as chaves são nomes de alunos e os valores são suas notas finais. O programa deve pedir ao usuário o nome de um aluno e exibir a nota desse aluno.
# Para esse desafio utilize
# ● Utilize if da seguinte maneira:
#   if aluno in notas:
#    Esse if tem o significado de = “Se aluno que foi digitado existe na lista = True”

notas = {"pedro": 8.5, "eduarda": 7.0, "sofia": 9.0, "renata": 6.5}
nomedoaluno = input("Digite o nome do aluno para consultar a nota: ")
if nomedoaluno in notas:
    print(f"A nota de {nomedoaluno} é {notas[nomedoaluno]}.")
else:
    print(f"Aluno '{nomedoaluno}' não encontrado.")
