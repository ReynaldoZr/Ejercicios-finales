# === Ejercicio 4: Escribir caracteres ASCII en 'ascii.txt' ===

# Abrimos o creamos el archivo ascii.txt en modo escritura
archivo = open("ascii.txt", "w", encoding="utf-8")

# Escribimos caracteres ASCII imprimibles del 32 al 126
for codigo in range(32, 127):
    linea = f"{codigo}: {chr(codigo)}\n"
    archivo.write(linea)

archivo.close()
print("El archivo 'ascii.txt' fue generado con la tabla de caracteres ASCII.")
