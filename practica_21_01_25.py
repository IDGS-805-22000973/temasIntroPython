import os

class CineDescuento:
    #Clase para el descuento 
    def tipoCobro(self, numBoletos):
        metodoPago = int(input("¿tienes tarjeta CINECO? 1. si / 2. no "))
        precio = numBoletos*12

        if numBoletos>5:
            precio *=0.85  
        elif numBoletos> 2:
            precio *=0.90
        if metodoPago== 1:
            precio *=0.90  
        return precio

class Comprador:
    #Datos del comprador junto a su metodo
    #Funcion para inicializar lo datos
    def __init__(self, nombre, numCompradores):
        #Inicializar los atributos de la clase 
        self.nombre=nombre #Almacenar los valores 
        self.numCompradores=numCompradores
        self.maxBoletos=numCompradores*7
    
    def comprarBoletos(self):
        #Todo lo del descuento
        cine_descuento=CineDescuento()
        total_compras=[]
        total_final=0
        while True:
            numBoletos = int(input("¿cuantos boletos quieres? cantidad maxima {}: ".format(self.maxBoletos)))
            while numBoletos > self.maxBoletos:
                print("no puedes comprar mas de {} boletos.".format(self.maxBoletos))
                print("\n1. Quitar boletos \n2. Agregar personas")
                opcion = int(input("Elige una opcion: "))

                if opcion == 1:
                    boletosRestar = int(input("¿cuantos boletos quieres quitar? "))
                    if boletosRestar < numBoletos:
                        numBoletos -= boletosRestar
                    else:
                        print("**no puedes quitar esa cantidad de boletos**")

                elif opcion==2:
                    personasAgregar = int(input("¿cuantas personas quieres agregar? "))
                    self.numCompradores += personasAgregar
                    self.maxBoletos = self.numCompradores*7
                    numBoletos = int(input("¿cuantos boletos quieres? cantidad maxima {}: ".format(self.maxBoletos)))
                if numBoletos <= self.maxBoletos:
                    break

            #Mando a llamar la clase Cinedescuento para usar la funcion tipoCobro con sus parametros
            total = cine_descuento.tipoCobro(numBoletos)
            #Resive toda una lista de datos
            total_compras.append("Nombre: {}, Total: ${}".format(self.nombre, total))
            total_final += total
            # print(f"**Total es de ${total}")
            
            seguir = int(input("¿quieres seguir comprando? 1. si / 2. no "))
            if seguir == 1:
                nombre = input("¿cual es tu nombre? ")
                numCompradores = int(input("*¿cuantos compradores?* "))
                self.__init__(nombre, numCompradores)
                
            elif seguir == 2:
                print("*** HAsta Luego**")
                os.system('cls')
                break
        texto = "Compras realizadas:\n"
        for compra in total_compras:
            texto += compra + "\n"
        texto += "Total Final de todas las compras: ${}".format(total_final)
        fichero = open('ticket.txt', 'w')
        fichero.write(texto)
        fichero.close()

def main():

    while True:
        nombre=input("¿cual es tu nombre? ")
        numCompradores=int(input("¿cuantos compradores? "))
        comprador=Comprador(nombre, numCompradores)
        comprador.comprarBoletos()
    
        ticket = open('ticket.txt', 'r')
        ticket.seek(0)  # Redirigir el cursor a la posicion de inicio
        texto1 = ticket.read()  # Volver a leer desde el inicio
        print(texto1)
        ticket.close()
        break

if __name__ == "__main__":
    main()
