#Leer el contenido del archivo de texto 'datos.txt' línea a línea.
archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()
#Este ejemplo es con for