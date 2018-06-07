""" Pedirdos numeros al usuario , realizar la suma, si la suma es mayo a 10 salir,
si es menor volver   pedir el par de numerossi se ingresa texto , salir tambien
"""

try:
    while True:
        one = int(input("First Number : ") )
        two = int(input("Second one _ ") )
        sum = one + two
        if sum < 10:
            print(f"the sum is {sum} ")
        else:
            break
except:
        pass
print("Bye")