# dEmonstração do uso de funções...
def adição(x, y):
    return x + y 
def subtração(x, y):
    return x - y 
print("Digite dois valores inteiros...")
n1 = int(input("x: "))
n2 = int(input("y: "))
op = input("qual operação (+ ou -)?")

if op == "+":
    z = adição(n1, n2)
    print("Resultado da soma:", z)
elif op == "-":
    z = subtração(n1, n2)
    print("Resultado da subtração:", z)
else:
    print("Opção digitada inexistente!")
    
