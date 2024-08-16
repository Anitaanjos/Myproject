#Atividades do dia 16/08/24
#breackfast
print("Vamos montar um carpadio personalizado")
cafedamanha = []
almoço = []
jantar = []

print("Cafe da manha")
for x in range(0, 3):
    opção = input(f'Digite a {x+1} opção:')
    cafedamanha.append(opção)
    if opção == "leite" or opção == "queijo" or  opção == "pão":
      print("Alimento não recomendado")
print("Eis, as opções escolhidas: ", cafedamanha)

print("Almoço")
for x in range (0, 4):
   opção = input(f'Digite a opção {x+1}:')
   almoço.append(opção)
   if opção == "camarão" or opção == "pimenta":
      print("Alimento não recomendado")
print("Eis, as opções escolhidas: ", almoço)

print("Jantar")
for x in range (0, 4):
   opção = input(f'Digite a opção {x+1}:')
   jantar.append(opção)
   if opção == "camarão" or opção == "pimenta":
      print("Alimento não recomendado")
print("Eis, as opções escolhidas: ", jantar)
 