#calcular IMC
print("digite seu peso")
peso = int(input())
print("digite sua altura")
altura = int(input())
IMC = peso / (altura ** 2)

if peso < 25:
    print("Acima do peso ideal")
elif peso > 18:
    print("Abaixo do peso ideal")
elif peso < 18 > 25:
    print("O seu peso está ok")