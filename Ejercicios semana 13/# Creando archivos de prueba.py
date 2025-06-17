# Creando archivos de prueba

with open("Parte1.txt", "w", encoding="utf-8") as f1:
    f1.write("Este es el contenido de parte 1.\n")

with open("parte2.txt", "w", encoding="utf-8") as f2:
    f2.write("Este es el contnido de parte 2.\n")

print("Archivos parte1.txt y parte2.txt creados con éxito.")