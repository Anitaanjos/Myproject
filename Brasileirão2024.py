#Tabela do brasileirão 2024
#Atividade 2 
time = input("digite o seu time: ")
posição = int(input("digite a posição do time: "))

if posição == 1:
    print("é campeão!")
elif posição > 1 and posição <= 6:
    print("Libertadores!")
elif posição > 6 and posição <= 12:
    print("Sul-americana")
elif posição > 12 and posição <= 16:
    print("Sem classificação")
elif posição >= 17 and posição <= 20:
    print("Rebaixado...")
else:
    print("Digite a posição correta!")