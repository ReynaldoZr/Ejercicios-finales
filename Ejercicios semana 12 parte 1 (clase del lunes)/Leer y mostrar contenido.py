# === Programa 2: Leer y mostrar el contenido de un archivo de texto ===

# Pide el nombre del archivo
nombre_archivo = input("Nombre del archivo que deseas leer: ")

# Abre el archivo en modo lectura
archivo = open(nombre_archivo, "r", encoding="utf-8")

# Lee el contenido completo
contenido = archivo.read()
archivo.close()

# Muestra el contenido
if contenido == "":
    print("El archivo está vacío.")
else:
    print("Contenido del archivo:")
    print(contenido)
