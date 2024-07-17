#Demonstração do uso de if/elif/else...
print("digite a sua idade")
IDADE = int(input())

if IDADE < 18:
    print("voce não é maior de idade!")
    print("não poderá realizar a operação")
elif IDADE >= 65:
    print("voce está perto de se aposentar")
    print("poderemos oferecer suporte técnico...")
else:
    print("voce é maior de idade")
    print("portanto poderá realizar as operações")

print("obrigado por optar pelos nossos serviços!")
