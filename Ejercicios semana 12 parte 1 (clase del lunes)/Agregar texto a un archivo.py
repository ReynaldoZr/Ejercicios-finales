# === Programa 3: Agregar texto a un archivo existente ===

# Pide el nombre del archivo
nombre_archivo = input("Nombre del archivo al que deseas agregar texto: ")

# Abre el archivo en modo agregar (append)
archivo = open(nombre_archivo, "a", encoding="utf-8")

# Pide texto hasta que se ingrese vacío
while True:
    linea = input("Escribe una línea (deja vacío para terminar): ")
    if linea == "":
        break
    archivo.write(linea + "\n")

archivo.close()
print(f"Texto agregado correctamente a '{nombre_archivo}'.")
# Fin del programa