#calcular IMC
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite sua altura"))
IMC = peso / (altura ** 2)

print(f"o seu IMC é {IMC}.")
if IMC > 25:
    print("Acima do peso ideal")
elif IMC < 18:
    print("Abaixo do peso ideal")
else:
    print("O seu peso está ok")