#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME

nome = str(input( "Diga seu nome:")).strip()
print("Seu nome tem Silva? {}" .format('silva' in nome.lower()))

