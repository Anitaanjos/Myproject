#Programa de jogo de futebol
#Atividade 4 
posição = input("disite a posição que voce joga: ")

if posição == "goleiro" or posição == "zagueiro" or posição == "lateral":
    print("Voce Joga na defesa")
elif posição == "volante" or posição == "meia":
    print("Voce joga no meio campo")
elif posição == "ponta" or posição == "atacante" or posição == "centro avante":
    print("Voce joga no ataque")
else:
    print("voce joga de teimoso...")

