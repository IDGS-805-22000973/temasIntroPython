from io import open

fichero=open('fichero.txt','r')
#readLine imprime los elementos en un arreglo con los valores de cada uno de los valores 
texto1=fichero.read()
print(texto1)
# funcion para reedirigir el cursro a la posision de inicio  fichero.seek(0)

print(texto1)
fichero.close()