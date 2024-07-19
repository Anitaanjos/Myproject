#Ordem numerica
#Atividadde 3 
x = int(input("digite o primeiro numero: "))
y = int(input("digite o segundo numero: "))
z = int(input("digite o terceiro numero: "))

#Verificar se estão em ordem crescente e decrescente
if x < y < z: 
    print("Os numeros estáo em ordem crescente.")
elif x > y > z: 
    print("Os numeros estão em ordem decrescente.")
else:
    print("Os numeros etão misturados!")