# === Programa 1: Guardar frases en un archivo de texto existente ===

# Pide el nombre del archivo
nombre_archivo = input("Nombre del archivo donde guardarás frases: ")

# Abre el archivo en modo escritura (sobrescribe lo que tenga)
archivo = open(nombre_archivo, "w", encoding="utf-8")

# Pide frases al usuario
while True:
    frase = input("Escribe una frase (deja vacío para terminar): ")
    if frase == "":
        break
    archivo.write(frase + "\n")

archivo.close()
print(f"Frases guardadas correctamente en '{nombre_archivo}'.")
