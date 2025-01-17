from io import open

texto = "Una lista con texto\n otra lista de texto"

fichero=open('fichero.txt','w')
fichero.write(texto)

cadena2="\n Esto es otra cadena"
fichero.write(cadena2)
cadena3="\Esto es otra cadena"
fichero.write(cadena3)
fichero.close()