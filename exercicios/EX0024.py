#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NAO COM O NOME 'SANTO'

cidade = str(input(" Diga o nome da cidade que nasceu")).strip()
print(cidade[:5].upper()== 'santo')

