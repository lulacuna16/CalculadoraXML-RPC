import xmlrpc.client
#crear un cliente del servidor
def menu(case,Cliente):
    if case==1:
        x=int(input("Ingrese x: "))
        y = int(input("Ingrese y: "))
        print(type(Cliente.suma(x, y)))
        print("{} + {} = {}".format(x,y,Cliente.suma(x,y)))
    elif case==2:
        x=int(input("Ingrese x: "))
        y = int(input("Ingrese y: "))
        print(type(Cliente.resta(x, y)))
        print("{} - {} = {}".format(x,y,Cliente.resta(x,y)))
    elif case==3:
        x=int(input("Ingrese x: "))
        y = int(input("Ingrese y: "))
        print(type(Cliente.multi(x, y)))
        print("{} * {} = {}".format(x,y,Cliente.multi(x,y)))
    elif case == 4:
        x = int(input("Ingrese x: "))
        y = int(input("Ingrese y: "))
        print(type(Cliente.div(x, y)))
        print("{} / {} = {:.2f}".format(x, y,Cliente.div(x, y)))
    else:
        print("Opcion no valida\n")
def verMenu(Cliente):
    seguir=True
    while (seguir):
        print("Eliga una operacion:")
        print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division")
        case=int(input("Opcion: "))
        menu(case,Cliente)
        print("Continuar?")
        cont=int(input("1.Si\t2.No\n"))
        if cont==1:
            seguir=True
        else:
            print()
            seguir= False

with xmlrpc.client.ServerProxy('http://192.168.1.64:56432',verbose=True) as Cliente:
    verMenu(Cliente)
