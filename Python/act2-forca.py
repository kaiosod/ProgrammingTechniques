import random

word_list = ["VERDE","CARRO","POSTE","GATO","CHAVE","FLORESTA","PASTELARIA","CORRIDA","CONTROLE","CAIXA","TELEFONE"]
count = -1
parts = ["0","./","|","\.","./","\."]
body = ["","","","","",""]

word = list(random.choice(word_list))
empty_list = ["-" for _ in word]
print(f"\n\n ADVINHE A PALAVRA!! \n\n {empty_list}")

while True:
    player = input("\nEscolha uma letra: ").upper()

    if player in word:
        print("\n -Acertou- \n")
        for i in range(len(word)):
            if word[i] == player:
                empty_list[i] = player
        print(empty_list)

        if not "-" in empty_list:
            print("---GANHOU!---")
            break

    else:
        print("\n -Errou- \n")
        count+=1
        if count == 6:
            print("---PERDEU!---")
            break
        
        body[count] = parts[count]
        print(f"  {body[0]} \n{body[1]}{body[2]}{body[3]}\n{body[4]} {body[5]}")

        
        
        