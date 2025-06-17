#Programa para calcular el total de ingresos generadosy el número de unidades vendidas de un producto determinado.
# especificado por el usuario.

#Un mensaje claro y sencillo de lo que se va a hacer en el programa
print()
print("Bienvenido al sistema de registro y análisis de ventas.\n")
print()
print("Primero vas a ingresar varias ventas, y luego podrás consultar cuántas unidades y cuánto dinero se generó por producto.\n")

#Parte 1: Registrar ventas

#Lo primero que hacemos es importar el archivo csv
import csv 

#Segundo, es crear o sobreescribir el archivo ventas.csv
with open("ventas.csv", mode="w", newline="") as archivo: # Mode w = Con esto hacemos que los datos que escribimos pasen al archivo csv 
    #Newline evitamos que se creen espacios en blancos 
    escritor = csv.writer(archivo)

    #Tercer paso, es crear la fila del encabezado
    escritor.writerow(["fecha", "producto", "cantidad", "precio"])

    #mandamos mensaje para las ventas

    print("Vamos a escribir ventas. Escribe 'fin' cuando termines.")

    #Cuarto paso, creamos un bucle con vacios para guardar los datos y un 'fin' para terminar
    while True:
        fecha = input("Fecha de la venta (ej: 2025-06-17): ")
        if fecha.lower() == "fin":
            break
        
        producto = input("Producto vendido: ")
        if producto.lower() == "fin":
            break
        
        cantidad = input("Cantidad vendida: ")
        if cantidad.lower() == "fin":
            break
        
        precio = input("Precio unitario del producto: ")
        if precio.lower() == "fin":
            break
        
        # Guardamos la fila en el archivo CSV
        escritor.writerow([fecha, producto, cantidad, precio])
        
        print("Venta registrada.\n")


#Parte 2: Analizar ventas

#Primero, mandamos a pedir el producto a analizar
producto_buscado = input("¿Qué producto quieres analizar?: ").lower()

#Segundo, creamos dos variables para acumular los resultados
unidades_totales = 0
ingresos_totales = 0.0

#Tercero, abrimos el archivo csv pero ahora en modo lectura en vez de escritor

with open("ventas.csv", mode="r") as archivo:
    lector = csv.reader(archivo) #creamos un lector que pueda leer el archivo linea por linea
    next(lector)  # Saltamos encabezado

    #Cuarto, creamos bucle  que lea cada línea (venta) del archivo.
    for fila in lector:
        fecha, producto, cantidad, precio = fila

        if producto.lower() == producto_buscado: #Comparamos el producto de la fila con el que el usuario pidió.
            unidades_totales += int(cantidad) #Sumamos esa cantidad vendida a nuestro contador.
            ingresos_totales += int(cantidad) * float(precio) #el dinero ganado con esa venta, lo sumamos al total y multiplicamos

#Quinto paso, mostramos los datos
print(f"\nSe vendieron {unidades_totales} unidades de '{producto_buscado}'.")
print(f"Se generaron ${ingresos_totales:.2f} en total.")
#Fin del programa
