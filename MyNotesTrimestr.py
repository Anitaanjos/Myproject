#Notas trimestrais
#atividade 2
x = int("digite a nota 1: ")
y = int("digite a nota 2: ")
z = int("digite a nota 3: ")
w = int("digite a nota 4: ")
SOMA = x + y + z + w 
MÉDIA = SOMA / 4 
print("A soma é", SOMA)
print(" a média é", MÉDIA)

print("digite sua nota")
NOTAS = int(input())

if NOTAS < 6:
    print("Aluno reprovado")
elif NOTAS >= 6:
    print("Aluno aprovado")
