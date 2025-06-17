# === Ejercicio 5: Leer y mostrar el contenido del archivo 'ascii.txt' ===

# Intentamos abrir el archivo ascii.txt en modo lectura
try:
    archivo = open("ascii.txt", "r", encoding="utf-8")
    contenido = archivo.read()
    archivo.close()

    if contenido == "":
        print("El archivo 'ascii.txt' está vacío. Primero ejecuta el ejercicio 4.")
    else:
        print("Contenido del archivo 'ascii.txt':")
        print(contenido)

except FileNotFoundError:
    print("El archivo 'ascii.txt' no existe. Ejecuta el ejercicio 4 para crearlo.")
