#Devolver programa de conversor de temperatura
print("converter de celsium para kelvin e fahrenheit...")
celsius = int(input("digite a temperatura"))
kelvin = celsius + 273
farenheit = (9 / 5 * celsius) - 32
print(f"a temperatura em kelvin será {kelvin}.")
print(f"a temperatuta em fahrenheit será {farenheit}.")