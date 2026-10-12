#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#SE ELE ULTRAPASSAR  80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE FOI MULTADO
#A MULTA VAI CUSTAR R$7,00 POR CADE KM ACIMA DO LIMITE

velocidade=int(input("Qual sua velocidade?"))
if velocidade <80:
    print("Tenha um Bom dia, dirija com segurança")
else:
    multa=(velocidade-80)*7
    print("Voce ultrapassou o limite da rodovia \n voce estava a {} KM/H \n "
          "entao pagara uma multa de R${:.2f}".format(velocidade,multa))

