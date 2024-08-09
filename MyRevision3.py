# revisão do match/case, logica de programaão geral...
print("O que voce achou dos nossos serviços???")
print("1.pessimo, 2.ruim, 3.razovel, 4.bom, 5.otimo...")
avaliação = int(input("Digite uma opção:"))

match avaliação:
    case 1:
        print("O serviço precisa melhorar muito!")
        print("Avaliação: reprovado!")
    case 2:
        print("o serviço precisa melhorar em alguns quesitos...")
        print("avaliação: reprovado")
    case 3:
        print("Nem bom, nem ruim...")
        print("Avaliação: recuperação!")
    case 4: 
        print("aceitavel no geral. embora possa melhorar!")
        print("Avaliação: Aprovada!")
    case 5:
        print("Perfeito melhor que isso estraga!")
        print("Avaliação: Aprovada1")
    case _:
        print("A opção digitada não esta correta!!")
print("Obrigado por usar nossos serviços...")