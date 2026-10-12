#FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADE UM DOS DIGITOS SEPARADOS.
#UNIDADE,DEZENA,CENTENA E MILHAR

num = int(input("insira um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(" Analisando seu numero {}".format(num))
print("Unidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))