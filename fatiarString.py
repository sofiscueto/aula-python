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
