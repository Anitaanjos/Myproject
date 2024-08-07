# Demonstração do uso de funções
def multiplicação(x, y):
    return x * y 
def divisão(x, y):
    return x / y 
print("Digite dois valores inteiros...")
n1 = int(input("x: "))
n2 = int(input("y: "))
op = input("qual operação (* ou /)?")

if op == "*":
    z = multiplicação(n1, n2)
    print("Resultado da multiplicação:", z)
elif op == "/":
    z = divisão(n1, n2)
    print("Resultado da divisão:", z)
else:
    print("Opção digitada inexistente!")