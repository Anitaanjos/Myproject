# revisão geral 
nome = input("Digite o seu nome:")
idade = int(input("digite a sua idade:"))
altura = float(input("digite a altura:"))

print(f"Meu nome é {nome}")
print(f"a minha idae é {idade}")
print(f"A minha altura é {altura}")

if idade < 18:
    print("Voce é menor de idade!!")
elif idade >= 18 and idade < 65:
    print("voce é maior de idade!!")
elif idade >= 65:
    print("Voce ja pode se aposentar!!")
else: 
    print("Nada mais a dizer...")