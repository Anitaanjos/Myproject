#Demostração de "case" para conversão de temperatura
print("Qual conversão voce deseja realizar...")
escolha = int(input("1. celsius / 2. kelvin / 3. fahrenheit"))
temperatura = int(input("digite o valor da temperatura: "))

match escolha :
    case 1:
        kelvin = temperatura + 273
        farenheit = (9 / 5 * temperatura) - 32
        print(f"a conversão de celsius para kelvin será {kelvin}.")
        print(f"A conversão de celsius para farenheit será {farenheit}")
    case 2:
        celsius = temperatura - 273
        farenheit = 1.8 * (temperatura - 273) + 32
        print(f"A conversão de kelvin para celsius será {celsius}.")
        print(f"A conversão de kelvin para farenheit será {farenheit}.")
    case 3:
        celsius = 5/9 * (temperatura - 32)
        kelvin = (temperatura - 32) / 1.8 + 273
        print(f"A conversão de farenheit para celsius será {celsius}. ")
        print(f"A conversão de farenheit para kelvin será {kelvin}.")

