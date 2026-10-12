#FAÇA UM PROGRAMA QUE  LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO
from datetime import date
ano=int(input("Qual ano voce quer analisar? Coloque 0 para o ano atual"))
if ano==0:
    ano=date.today().year
if ano % 4==0 and ano % 100!=0 or ano % 400==0:
    print("O ano {} ele é bissexto".format(ano))
else:
    ano % 4==1
    print("O ano {} ele não é bissexto".format(ano))

