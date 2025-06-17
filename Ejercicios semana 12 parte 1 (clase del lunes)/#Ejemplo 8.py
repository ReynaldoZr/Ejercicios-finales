#Ejemplo 8
"""
Ejemplo simple de cómo leer un archivo completo en Python 3
@author parzibyte
"""
nombre_archivo = "datos.txt"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("El contenido es:", contenido)
