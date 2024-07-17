#dias da semana
#  atividade 1
print("digite um dia da semana")
print("1. domingo")
print("2. Segunda-feira")
print("3. Terça-feira")
print("4. Quarta-feira")
print("5. Quinta-feira")
print("6. Sexta-feira")
print("7. Sabado")
ESTADO = int(input())

match ESTADO:
    case 1:
        print("dia de descansar e aproveitar com a familia")
    case 2:
        print("inicio de semana, trabalhe mas não deixe de beber água")
    case 3:
        print("trabalhe mas não se esqueça de focar nos treinos")
    case 4:
        print("se alimente bem e não desista")
    case 5:
        print("quinta feira é igual calcinha, não é o que a gente quer mas está perto...")
    case 6:
        print("sextouu, trabalhe e tome aquela breja")
    case 7:
        print("sabadouuu, acorde cedo e vá a feira comer um pastel com caldo de cana")
    case _:
        print("opção não identificada")