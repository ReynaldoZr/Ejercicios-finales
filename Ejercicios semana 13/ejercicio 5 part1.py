# Ejercicio 5: Concatenación de archivos

# Abrir y leer el contenido de parte1.txt
with open("parte1.txt", "r", encoding="utf-8") as arch1:
    contenido1 = arch1.read()

# Abrir y leer el contenido de parte2.txt
with open("parte2.txt", "r", encoding="utf-8") as arch2:
    contenido2 = arch2.read()

# Combinar ambos contenidos
contenido_completo = contenido1 + contenido2

# Escribir el contenido combinado en completo.txt
with open("completo.txt", "w", encoding="utf-8") as archivo_completo:
    archivo_completo.write(contenido_completo)

print("Archivos comnbinados correctamente en completo.txt")