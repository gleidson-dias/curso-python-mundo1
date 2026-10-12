#print("\033[7;33;44mOla mundo\033[m")

#a=1
#b=2
#print("os valores sao \033[33;44m{} e \033[31;44m{} \033[m".format(a,b))

#nome="Gleidson"
#print("Muito prazer em te conhecer, {}{}{} !!!".format("\033[1;34;41m",nome,"\033[1;34;41m"))

nome="Gleidson"
cores= {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;40m'}
print("Muito prazer em te conhecer, {}{}{} !!!".format(cores['pretoebranco'],nome,cores['limpa']))

