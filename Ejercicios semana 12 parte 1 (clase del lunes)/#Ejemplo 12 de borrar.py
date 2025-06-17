#Ejemplo 12 de borrar

# Eliminar líneas del archivo

# Abrir el archivo y leer las líneas
with open("datos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# Filtrar las líneas que no contienen "Segunda línea"
lineas_filtradas = [linea for linea in lineas if linea.strip() != "Segunda línea"]

# Sobrescribir el archivo con las líneas filtradas
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas_filtradas)
