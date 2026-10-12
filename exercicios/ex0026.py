#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO O TECLADO E MOSTRE:
#QUANTAS VEZES APARECE A LETRA "A"
#EM QUE POSIÇÃO ELA APARECE PELA A PRIMEIRA VEZ
#EM QUE POSIÇÃO ELA APARECE PELA A ULTIMA VEZ

frase= str(input("Digite uma frase:")).upper().strip()
print("A letra A aparece {} vezes na frase".format(frase.count('A')))
print("A primeira vez que o A aparece é na posição {}".format(frase.find('A')+1))
print("A ultima vez que o A apareceu foi na posição {}".format(frase.rfind('A')+1))




