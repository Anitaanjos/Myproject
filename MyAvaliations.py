#avaliações
#Atividade 5
execução = input("O serviço foi feito (sim/Não)? ")
avaliação = int(input("Qual a nota da avaliação (1/5)? "))


if execução == "sim" and avaliação == 1:
    print("O serviço foi pessimo!")
elif execução == "sim" and avaliação == 2:
    print("O serviço foi ruim!")
elif execução == "sim" and avaliação == 3:
    print("O serviço foi razoavel!")
elif execução == "sim" and avaliação == 4:
    print("O serviço foi bom!")
elif execução == "sim" and avaliação == 5:
    print("O serviço foi exelente!")
else:
    if execução == "não" and avaliação == 0:
        Reclamação = input("Digite a sua reclamação: ")
    else:
        print("as suas avaliações não fazem sentido!")