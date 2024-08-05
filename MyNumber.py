# Demonstração do uso da estrutura repetitiva...
numero = 1
while numero >= 0:
    print("Digite um numero negativo para sair:")
    numero = int(input())
    continue
    print("este texto não será exibido1 mas...")
else:
    print("O numero digitado foi:", numero)