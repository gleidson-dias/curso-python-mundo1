#DESENVOLVA UMM PROGRAMA QUE PERGUNTE A DISTANCIA DE UM VIAGEM EM KM.
#CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATE 200KM
#E 0,45 PARA VIAGENS MAIS LONGAS

distancia=float(input("Quantos km tem sua viagem ?"))
if distancia<=200:
    valor=distancia*0.50
    print("Você pagara R${:.2f} na sua viagem pois ate 200KM a sua passagem sai por R$0.50".format(valor))
else:
    distancia>=200
    valor=distancia*0.45
    print("Você pagara R${:.2f} na sua viagem, como sua viagem é mais longa a sua passagem sai por R$0.45".format(valor))
