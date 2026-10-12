#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR EM UM NUMERO INTEIRO ENTRE 0 E 5
#E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO ESCOLHIDO PELO O COMPUTADOR
# O PROGRAMA DEVERA ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU
from random import randint
from time import sleep
computador = randint(0,5)
print("-=-"*20)
print(" Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
jogador = int(input("Em qual numero pensei?"))
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("Voce acertou,PARABENS VOCE VENCEU")
else:
    print("Voce errou o numero escolhido foi {},tente novamente".format(computador))






