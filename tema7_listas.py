lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes","Martes","Miercoles"]
lista4=["Juan",45,1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0])

x=0
suma=0

while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1

print("La suma es: {}".format(suma))


print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

#Agregara valores a una lista con un ciclo for

lista5=[]
for x in range(1):
    valor=int(input("Ingresa un valor: "))
    lista5.append(valor)

print(lista5)

#Eliminar elementos de una lista

print(lista1)
lista1.pop()
print(lista1)


# Crea un programa para pedir una catidad n numeros y almacenarlos en un arreglo la salida debe ser la siguiente
#Lista completa : xxxxxxx
#Numeros pares de la lista : aaaaaaaa
#Numeros impares de la lisa : rrrrrrr


print("Ingresa el tamaño del arreglo")
i=0
tamañoA=int (input(""))
lista6=[]
listaPar=[]
listaImpar=[]
a=0

for i in range(tamañoA):
    valor=int(input("Ingresa los valores del arreglo con tamaño {}: ".format(tamañoA)))
    lista6.append(valor)

for a in range(len(lista6)):
    if lista6[a] % 2 == 0 :
        listaPar.append(lista6[a])

    else:
        listaImpar.append(lista6[a])


print("Valores en el arreglo {}".format(lista6))
print("Valores impares {}".format(listaImpar))
print("Valores pares  {}".format(listaPar))



#Ordenar los valores de un arreglo
"""
lista.sort()
print(lista1)
lista1.reverse()
print()

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)
"""