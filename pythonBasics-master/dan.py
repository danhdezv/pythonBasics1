print("hello world")

x = 1
while x < 5:
    print("x: ", x)
    x = x + 1
print("------")
heigth = 5
#*****
#****
#***
#**
#*

while heigth > 0:
    aux = heigth
    while aux > 0:
        print("*",end="")
        aux = aux -1
    heigth = heigth -1
    print("")
#########3
heigth = int( input("N: ") )
while heigth > 0:
    print("*"*heigth )
    heigth -= 1

