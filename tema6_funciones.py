import os
def funcion1():
    os.system('cls')
    print ("Dame dos numeros")
    num1 = int (input("Primer numero: "))
    num2 = int (input("Segundo numero: "))
    res=num1+num2
    print("La suma de {} y {} es {}".format(num1,num2,res))
    

def funcion2():
    print("Hola sou funcion 2")


def run():
    os.system('cls')
    print("Menu de operaciones")
    print("1 Suma de operaciones")
    print("2 otra opcion")
    print("Salir")
    opcion = int(input("Ingresa una opcion"))
    if opcion == 1:
        funcion1()
    elif opcion == 2:
        funcion2()
    


if __name__ == '__main__':
    run()

    


