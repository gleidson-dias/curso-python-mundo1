
n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
media=(n1+n2)/2
print("A sua media é {:.1f}".format(media))
if media >=6:
    print("A sua media esta boa, PARABENS!!!!")
else:
    print("A su media esta ruim, precisa melhorar. ESTUDE!!!")
