# atividade 1 do dia 09/08 cliente de bancos
print("Olá, bom dia")
print("seja bem vindo(a) ao banco online privt")

nome = input("digite o seu nome")
datadenascimento = input("Digite sua data de nascimento")
rg = input("Digite seu cpf/RG")
dinheiro = input("Digite o valor de abertado de conta")
print("Sua conta foi aberta...")
print("Parabéns por abrir uma conta com a privt!!!")

print("qual operação voce deseja realizar...")
print("1.consulta e saldo, 2.Deposito, 3.Saque")
opção = int(input("Digite uma opção..."))

match opção:
    case 1:
        print("vou verificar o saldo da sua conta.")
        saldo = float(input("Digite o seu saldo:"))
        if saldo >= 1:
             print("Seu saldo está positivo!!!")
        elif saldo <= 0:
            print("Seu saldo está no negativo")
    case 2:
        deposito = float(input("Digite o valor de deposito:"))
        print("seu deposito foi feito!")
    case 3:
        print("Digite o valor que voce deseja retirar...")
        print("seu saque foi realizado!!")
