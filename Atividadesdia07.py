#Atividade 01 do dia 07/08 ...
def apresentar():
    print("minha idade é", MyAge, "anos")
    return
def conferir(x):
    if x >= 18:
        print("Voce é maior de idade!!")
        print("aqui esta uma lista com carros e seus respectivos preços...")
        lista_carros()
    else:
        print("voce é menor de idade!!")
        print("Aqui esta a lista dos programas para vc assistir...")
        lista_programasinfantis()
def lista_carros():
    # Lista de carros e seus preços
    carros = {
        "Toyota Corolla": "R$ 100.000",
        "Honda Civic": "R$ 120.000",
        "Ford Focus": "R$ 110.000",
        "Chevrolet Cruze": "R$ 115.000",
        "Hyundai Elantra": "R$ 105.000"
    }
    print("Lista de carros e seus preços:")
    for carro, preco in carros.items():
        print(f"{carro}: {preco}")
def lista_programasinfantis():
    # Lista de programas infantis
    programas = [
        "Peppa Pig",
        "Patrulha Canina",
        "Dora, a Aventureira",
        "Galinha Pintadinha",
        "Mundo Bita"
    ]

    print("Lista de programas infantis:")
    for programa in programas:
        print(programa)

MyAge = int(input("Digite sua idade: "))

apresentar()
conferir(MyAge)
    