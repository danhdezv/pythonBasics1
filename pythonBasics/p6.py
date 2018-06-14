""" Functions """

def average(the_list):
    return sum(the_list) / len(the_list)

my_list = []

while True:
    num = input("")
    if(num.isnumeric() ):
        my_list.append(int(num))
    else:
        break
    prom = average(my_list)
    print("promedio: ", prom )

    

