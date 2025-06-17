# Este programa es un diario personal hecho por un estudiante de primer ingreso
# Cada vez que se ejecuta, guarda lo que escribo junto con la fecha y hora en un archivo de texto

# Paso 1: Importar la librería para obtener fecha y hora
import datetime

# Paso 2: Pedirle al usuario que escriba algo para guardar en el diario
entrada = input("Escribe tu entrada para el diario: ")

# Paso 3: Obtener la fecha y hora actual
ahora = datetime.datetime.now()
fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")  # Formato bonito

# Paso 4: Abrir el archivo 'diario.txt' en modo agregar (así no se borra lo anterior)
archivo = open("diario.txt", "a")

# Paso 5: Escribir la fecha y hora y luego lo que el usuario escribió, todo en el archivo
archivo.write("Fecha y hora: " + fecha_hora + "\n")
archivo.write(entrada + "\n")
archivo.write("-" * 40 + "\n")  # Línea para separar entradas

# Paso 6: Cerrar el archivo
archivo.close()

# Mostrar mensaje final
print("Tu entrada ha sido guardada en el diario. 😊")
# Fin del programa