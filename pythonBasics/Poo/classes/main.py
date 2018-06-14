"""
BANK_ACCOUNT
"""


class Bank_Account:
    def __init__( self ):
        self.balance = 0
    
    def deposit( self, amount ):
        self.balance += amount
    
    def print_balance(self):
        print( " Tu balance: ", self.balance)

    def retirar_m(self, retiro):
        if( self.balance >= retiro):
            self.balance -= retiro
        else :
            print("No puedes retirar esa cantidad")

cuenta1 = Bank_Account()
"""
cuenta1.print_balance()
cuenta1.deposit(1000)
cuenta1.print_balance()
print("voy a retirar 1100")
cuenta1.retirar_m(1100)
cuenta1.print_balance()
print("voy a retirar 100")
cuenta1.retirar_m(100)
cuenta1.print_balance()

cantidad = int ( input("introduce cantidad:  ") )
cuenta1.deposit(cantidad)
cuenta1.print_balance()
"""
opc = 0
print("Opcion 1 : Depositar")
print("Opcion 2 : Imprimir balance")
print("Opcion 3 : Retirar")
while (opc >= 0 and opc <= 3  ):
    opc = int ( input("Que operacion quiere realizar:  ") )
    if( opc == 1 ):
        cantidad = int ( input("introduce cantidad a depositar :  ") )
        cuenta1.deposit(cantidad)
    elif ( opc == 2 ):
        cuenta1.print_balance()
    elif ( opc == 3 ):
        cantidad = int ( input("introduce cantidad a retirar :  ") )
        cuenta1.retirar_m(cantidad)
    elif ( opc == 0 ):

        print("_________MENU___________")
        print("Opcion 1 : Depositar")
        print("Opcion 2 : Imprimir balance")
        print("Opcion 3 : Retirar")
        print("_______________________")
    else:
        print("opc no valida")

