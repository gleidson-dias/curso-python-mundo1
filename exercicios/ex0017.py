from math import sqrt,pow
num1=float(input(" Diga o comprimento do caateto oposto"))
num2=float(input(" Diga o comprimento do cateto adjacente"))
hipotenusa=sqrt(pow(num1,2)+pow(num2,2))
print(" A hipotenusa mede {:.0f} metros".format(hipotenusa))


