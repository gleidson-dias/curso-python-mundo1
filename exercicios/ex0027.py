#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E ULTIMO NOME SEPARADAMENTE
# EX: ANA MARIA DE SOUZA
# PRIMEIRO NOME: ANA
# ULTIMO NOME: SOUZA

n=str(input("Digite seu nome completo:")).strip()
nome=n.split()
print("Seu primeiro nome ée {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[len(nome)-1]))
