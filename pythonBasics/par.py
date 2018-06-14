#Numero par
"""
numero = int(input("Introduce Numero: ") )

if ( (numero%2) == 0):
    print ("numero es par")
else:
    print("Numero es impar")

"""


"""
El usuario introduce dos valores un texto y un numero
si el texto es igual a "suma" y el numero es mayor a 10 imprimir la sumtoria de si mismo hasta llegar a 100
11+ 11+ 11 ------
cualquier caso diferente de entrada salir del programa
"""

numero = int(input("Introduce Numero: ") )
texto = str( input("Introduce Texto: " ) )

if ( numero > 10 and texto == "suma" ):
    print("ok")
    suma = numero
    while( suma < 100) :
        print("suma " , suma)
        suma = numero + suma

else :     
    print("bad")

