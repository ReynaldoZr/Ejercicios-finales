# Ejercicio 4: Lector de Datos CSV
# Este programa lee productos desde el archivo Libro1.csv y muestra su información

# Paso 1: Abrimos el archivo "Libro1.csv" en modo lectura
try:
    with open("Libro1.csv", 'r') as archivo:
        # Paso 2: Recorremos el archivo línea por línea
        for linea in archivo:
            # Paso 3: Eliminamos el salto de línea al final
            linea = linea.strip()

            # Paso 4: Dividimos la línea por comas
            datos = linea.split(',')

            # Paso 5: Aseguramos que haya 3 elementos (nombre, precio, stock)
            if len(datos) == 3:
                nombre = datos[0]
                precio = datos[1]
                stock = datos[2]

                # Mostramos la información formateada
                print(f"Producto: {nombre} | Precio: ${precio} | Stock: {stock} unidades")
            else:
                print("Línea con formato incorrecto:", linea)

# Paso 6: Si el archivo no existe, mostramos un mensaje de error
except FileNotFoundError:
    print("Error: No se encontró el archivo 'Libro1.csv'. Verifica que esté en la misma carpeta que este código.")
# Fin del programa