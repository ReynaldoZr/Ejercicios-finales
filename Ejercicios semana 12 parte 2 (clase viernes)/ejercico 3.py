# Ejercicio 3: Generador de Listas de Compras

# Este programa permite al usuario crear una lista de compras y guardarla en un archivo

# Paso 1: Abrimos el archivo 'compras.txt' en modo escritura ('w')
# Esto crea el archivo o borra el contenido anterior si ya existía
with open("compras.txt", 'w') as archivo:
    
    # Paso 2: Creamos un bucle infinito
    while True:
        # Paso 3: Pedimos al usuario que ingrese un producto
        producto = input("Ingrese un producto (o escriba 'fin' para terminar): ")

        # Paso 4: Si el usuario escribe 'fin', se rompe el bucle
        if producto.lower() == "fin":
            break

        # Paso 5: Si no es 'fin', escribimos el producto en el archivo con salto de línea
        archivo.write(producto + '\n')

# Paso 6: Fuera del bloque 'with', el archivo ya está cerrado automáticamente
# Notificamos al usuario que la lista fue guardada
print("La lista de compras ha sido guardada en 'compras.txt'.")
# Fin del programa
