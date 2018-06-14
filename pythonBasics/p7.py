"""
iterativamete se pediran numeros al usuario seguidos por un string que puede ser
eñ signo "+" o "-" a partir de ahi el siguiente elemento insertado
se sumara o restara deacuerdo al visor del signo-.... el programa terminara cuando se insertte 
otro string que sea distinto de + o -
1 + 5 6
9 - 5
"""
# Calculadora
def arirmetica(n1, n2,op ):
    if(op == "+" ):
        return n1+n2
    if(op == "-"):
        return n1-n2
    else:
        return "Operador no valido"

signo = "+"

#while( signo == "+" or signo == "-" ):
numero1 = int ( input("introduce numero:  ") )
signo  = input("introduce operador :  ")
numero2 = int ( input("introduce 2do numero:  ") )
print("_____________")
print(" ",arirmetica(numero1,numero2,signo))

rest = arirmetica(numero1,numero2,signo)

while( signo == "+" or signo == "-" ):
    signo  = input("introduce operador :  ")
    numero1 = int ( input("introduce numero:  ") )
    rest = arirmetica(rest,numero1,signo)
    print("______")
    print (rest)




