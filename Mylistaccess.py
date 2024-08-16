#demonstração de acesso das listas...

print("vou montar a marmita com 5 alimentos!")
marmita = ("feijão", "arroz", "legumes", "salada", "carne")
print("eis, a nossa recomendação", marmita)

resposta = input("voce quer montar uma marmita diferente (S/N)?")
if resposta == "S":
    for x in range(0,5):
        print(f'digite o {x+1}o. item do cardapio:')
        marmita[x] = input()
    print("A marmita montada foi:", marmita)
    print("O tres primeiros itens foram:", marmita[0:3])
    print("O ultimo item da marmita foi:", marmita[-1])
else:
    print("ok, voce decide...")
    
