# Ejercicio 2: Contador de Líneas
# Objetivo: Contar cuántas líneas tiene un archivo de texto

# Paso 1: Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo (ejemplo: poema.txt): ")

# Paso 2: Intentar abrir el archivo usando try...except
try:
    # Paso 3: Abrimos el archivo en modo lectura ('r')
    with open(nombre_archivo, 'r') as archivo:
        # Paso 4: Leemos todas las líneas del archivo como una lista
        lineas = archivo.readlines()
        
        # Paso 5: Calculamos cuántas líneas tiene la lista
        cantidad_lineas = len(lineas)
        
        # Mostramos la cantidad de líneas al usuario
        print("El archivo tiene", cantidad_lineas, "líneas.")

# Paso 6: Si el archivo no se encuentra, mostramos un mensaje de error
except FileNotFoundError:
    print("Error: El archivo no existe. Por favor verifica el nombre e intenta de nuevo.")
# Fin del programa