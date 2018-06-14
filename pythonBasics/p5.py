#EStructuras de datos 
"""
    Dictionariees       Diccionarios
    lists               listas
    Tuples      
    Sets
"""
"""
lista = [2,4,8,16,33,44,66,77]
for n in lista[1:4]:
    print(n)
print (lista)
for n in range(4):
    print(lista[n] )

for x in range(5):
    print(x)
print("-----")
for x in range(2, 30, 3):
  print(x)

print("____")

for x in range(2,6):
    print(x)

texto = "1234567"

for a in range( len(texto ) ):
    print(a, " ", texto)


"""
"""
values = [] 
values.append(1)
values.append(2)
values.append(3)
print(values)
values.reverse()
print(values)
"""
"""
El usuario tendra que introducir valores numericos, los cuales se almacenaran
para despues sacar el promedio
y mostrarlo cuando el valor introducido no sea numero
"""
print ("No para salir")
numero = input("Introduce numero: ")

promedio = []
while (numero.isnumeric()):
    promedio.append(numero)
    numero = input("Introduce numero: ")

print("numeros introducidos.... " , promedio)

suma = 0
for x in range( len(promedio ) ):
    suma +=  int( promedio[x] )


print("suma", suma)

print("promedio = ", suma / len(promedio) ) 


