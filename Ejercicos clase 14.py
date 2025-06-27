

ARCHIVO= "estudiantes.txt"
CLAVE= "Admin123" #Puedes cambiar esta clave

#Funcion de autenticacion
def inicio():
    print("INICIO DE SESION")
    intento= input("Ingresa la contraseña")
    if intento == CLAVE:
        print("ACCESO PERMITIDO\n")
        return True
    else: print("contraseña incorrecta. El acceso esta denegado.\n")
    

