n1=float(input("Digite a altura da parede"))
n2=float(input("Digite a largura da parede"))
area=n1*n2
print("A dimensao da sua parede é de {}x{} e a area dela é de {:.2f}".format(n1,n2,area))
litros=area//2
print("Para pintar a sua parede sera necesario {} litros de tinta".format(litros))

