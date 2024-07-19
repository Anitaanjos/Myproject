#Atividade 1 notas escolares...
nota1 = float(input("digite a note 1: "))
nota2 = float(input("digite a nota 2: "))
média = (nota1 + nota2) / 2 
recuperação = média < 4 

if média < 4:
    print("Aluno reprovado")
elif média > 6:
    print("Aluno aprovado direto")
elif média > 4 < 6:
    print("Aluno em recuperação")

#solicitação a nota de recuperação ao usuario
    nota_recuperação = float(input("digite a nota de recuperação: "))

#verifica se a nota é menor que 5
    if nota_recuperação < 5:
        print("reprovado na recuperação")
    else:
        print("aprovado na recuperação")