# exercicio 1 do slide 10 do dia 14/08/24
print("eis, a média e a soma de 1 a 6:")
teclado = [[1, 2, 3],
           [4, 5, 6]]
numeros = []
print("Digite os numeros que vc quer somar")
for x in range(0, 2):
    numeros.append(input(f'Digite os digitos{x+1}:')) and numeros.append(input(f'digite os digitos{x * 1}:'))

for x in range(0, 2):
    for y in range(0, 2):
        print(x + y)