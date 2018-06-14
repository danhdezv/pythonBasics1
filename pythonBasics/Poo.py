
class Antena:
    color = ""
    longitud = ""

    def func_antena_print(self):
        print("color: \t" , self.color ,  "\tlontitud: \t" , self.longitud)

    

class Pelo:
    color = ""
    textura = ""

    def func_Pelo_print(self):
        print("color: \t" , self.color ,  "\tTextura: \t" , self.textura)


class Ojo:
    forma = ""
    color = ""
    tamaño = ""
    def func_Ojo_print(self):
        print("Forma: \t" , self.forma ,  "\tcolor :\t" , self.color , "\tTamaño:\t", self.tamaño)

class Objeto:
    color = ""
    tamaño = ""
    aspecto = ""
    antenas = Antena() # 
    ojos = Ojo()
    pelos = Pelo()

    #FUNCION FLOTAR
    def funcfloat( self ):
        print("I'm floating!")

    #FUNCION IMPRIMIR ATRIBUTOS
    def func_Print(self):
        print("El objeto es de color:\t \t",self.color)
        print("El objeto tiene un tamaño: \t",self.tamaño)
        print("El objeto tiene un aspecto: \t",self.aspecto)
        print("_________________________________________")
        print("\t El objeto Tiene antenas..." )
        self.antenas.func_antena_print()
        print("\t El objeto Tiene Ojos..." )
        self.ojos.func_Ojo_print()
        print("\t El objeto Tiene Pelos..." )
        self.pelos.func_Pelo_print()
        print("_________________________________________")
        
marihuano = Objeto()
marihuano.funcfloat()
#objeto llenar
marihuano.color = "Verde"
marihuano.tamaño = "Gigante"
marihuano.aspecto = "Marciano"
marihuano.antenas.color = "Azul"
marihuano.antenas.longitud = "Grande"
marihuano.ojos.color = "Rojos"
marihuano.ojos.forma = "Redondos"
marihuano.pelos.color = "Azules"
marihuano.pelos.textura = "Aspera"

#imprime objeto
marihuano.func_Print()

