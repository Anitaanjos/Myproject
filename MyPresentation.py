# Demonstração do uso de funções...
def apresentar():
    print("meu nome é", Myname, ".")
    print("Minha altura é", Myheigh, "metros")
    print("Minha idade é", MyAge , "anos")
    return
def conferir(x):
    if x >= 18:
        print("Voce é maior de idade!")
    else:
        print("ops, menor de idade não pode!")
    return
Myname = str(input("Digite o seu nome: "))
Myheigh = float(input("Digite sua altura: "))
MyAge = int(input("Digite sua idade: "))

apresentar()
conferir(MyAge)