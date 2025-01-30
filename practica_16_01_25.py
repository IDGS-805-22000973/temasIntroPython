# la Distancia entre los dos puntos 
#pido los dos puntos 
import math

print("Calculadora de la distancia entre dos puntos \n Ingresa las coordenadas")

print("Ingresa los valores del primer punto")

x1=int(input("Ingresa el valor de x1 "))
y1=int(input("Ingresa el valor de y1 "))

print("Ingresa los valores del segundo punto")

x2=int(input("Ingresa el valor de x2 "))
y2=int(input("Ingresa el valor de y2 "))


distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia es {}".format(distancia))
