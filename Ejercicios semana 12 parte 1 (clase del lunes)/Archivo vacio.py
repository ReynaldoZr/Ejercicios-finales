# === Programa 0: Crear un archivo vacío ===

# Pide el nombre del archivo a crear
nombre = input("Escribe el nombre del archivo que deseas crear (ejemplo: frases.txt): ")

# Crea el archivo vacío (modo escritura 'w')
archivo = open(nombre, "w", encoding="utf-8")
archivo.close()

print(f"Archivo '{nombre}' creado correctamente. Ahora puedes usarlo en otros ejercicios.")
# Fin del programa