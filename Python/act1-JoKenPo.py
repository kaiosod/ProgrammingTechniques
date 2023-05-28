import random

jogador = 0

while(jogador != 3):
    maquina = random.choice(["Pedra","Papel","Tesoura"])
    jogador = int(input("\n\nEscolha \n 0 para Pedra \n 1 para Tesoura \n 2 para Papel \n 3 para Sair do Jogo \n:"))


    if (jogador == 0):
        jogador = "Pedra"
    elif (jogador == 1):
        jogador = "Papel"
    elif (jogador == 2):
        jogador = "Tesoura"
    elif (jogador == 3):
        print("O Jogo acabou")
        break
    else:
        print("\nOpção Inválida, escolha novamente\n")
        # while(jogador != 1 or jogador != 2 or jogador != 3):
        while(jogador>3):
            jogador = int(input("=== \n\n Escolha \n 1 para Pedra \n 2 para Tesoura \n 3 para Papel \n\n:"))
            if (jogador == 0):
                jogador = "Pedra"
                break
            elif (jogador == 1):
                jogador = "Papel"
                break
            elif (jogador == 2):
                jogador = "Tesoura"
                break

    print("\n\n" + jogador +" x "+ maquina)

    if(jogador=="Pedra" and maquina=="Tesoura"):
        print("Ganhou !!")
    elif(jogador=="Pedra" and maquina=="Papel"):
        print("Perdeu")
    elif(jogador=="Papel" and maquina=="Pedra"):
        print("Ganhou")
    elif(jogador=="Papel" and maquina=="Tesoura"):
        print("Perdeu")
    elif(jogador=="Tesoura" and maquina=="Pedra"):
        print("Perdeu")
    elif(jogador=="Tesoura" and maquina=="Papel"):
        print("Ganhou")
    elif (jogador == jogador):
        print("Empate")

