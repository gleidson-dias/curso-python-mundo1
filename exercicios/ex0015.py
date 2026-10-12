dias=int(input("Quantos dias ficou com o carro?"))
km=float(input("quantos km voce rodou com o carro?"))
pagamento=(dias*60)+(km*0.15)
print("Você ficou {} dias com o carro, e percorreu {} kilometros com ele, entao voce pagara R${}".format(dias,km,pagamento))

