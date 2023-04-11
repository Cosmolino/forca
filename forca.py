import os
contadora = 0
while(contadora == 0):

    #Jogo da forca python 3
    #Desenvolvedor: Tiago m.
    #Versão: 1.0

    #Menu de boas vindas
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************")

    palavra_secreta = "Maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    #Variáveis de validação e verificação do jogo
    enforcou = False
    acertou = False
    erros = 0

    #Controle de fim de jogo "Enquanto"
    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index +=1

        else:
            erros += 1

        if erros==6:
            enforcou = True

            if "_" not in letras_acertadas:
                acertou = True
        
        print(letras_acertadas)
        print('Chutes errados', erros)

    os.system("cls")

    
        
