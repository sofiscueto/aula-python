diaMaxIncri = 28
idadeMin = 14
idadeMax = 17

indicacao = True
listaEspera = False

idadeMarcelo = 15
diaInscriMarcelo = 29

def validarInscri():
    if diaInscriMarcelo <= diaMaxIncri or indicacao:
        print("Marcelo tem indicação de seu professor, então poderá fazer sua inscrição!")
    else:
        print("Marcelo perdeu a data de inscrição!")
        return False
    
    if not listaEspera:
        print("Marcelo não está na lista de espera!")
    else:
        print("Marcelo está na lista de espera!")
        return False

    if idadeMarcelo <= idadeMin and idadeMarcelo >= idadeMax:
        print("Marcelo tem a idade permitida para a inscrição!")
    else:
        print("Marcelo não poderá realizar sua inscrição!")
        return False
    return True

inscricao = validarInscri()
if(inscricao):
    print("Foi possível fazer a inscrição de Marcelo!")
else:
    print("Não foi possível fazer a inscrição de Maecelo")
