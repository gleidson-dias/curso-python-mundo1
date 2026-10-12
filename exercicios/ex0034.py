#ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SALARIOS MAIOR QUE R$1.250,00, CALCULE UM AUMENTO DE 10%.
#PARA INFERIORES OU IGUAIS, O AUMENTO DE 15%.

salario=float(input("Digite seu salario : R$ "))
if salario >=1250:
    aumento=salario*10/100
    novo=salario+aumento
    print(" O seu salario foi de R${:.3f} para R${:.3f} com o aumento de 10%".format(salario,novo))
else:
    aumento= salario*15/100
    novo=salario+aumento
    print("O seu novo salario foi de R$ {:.3f} para R${:.3f} com aumento de 15%".format(salario,novo))

