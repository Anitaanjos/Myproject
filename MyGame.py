# Atividade 2 do dia 07/08
# Jogo de par ou impar
print("Vamos brincar de par ou impar!!!")
x = print("Digite um numero:")
x = float(input())
y = print("eu escolhi 5")
y = 5
print("Vamos somar nossos numeros")
print("Se a soma der par vc ganha, se der impar eu ganho!!")
def adição(x, y):
    return x + y 
soma = x + y 
print("O resultado da operação é", soma)

if soma % 2 == 0:
    print("O resultado deu par!")
    print("Parabens voce ganhou!!!")
else:
    print("O resultado deu impar!")
    print("Eu ganhei!!")