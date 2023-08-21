"""
Proyecto creado en MVC backend
-Abrir asistente
-Login y Registro
-Creación, Edición, Eliminado y Listas de datos
"""

print("""
Acciones Disponibles:
    - Registro
    - Login
""")

accion = str(input("Ingresa el comando que desee utilizar: "))

if accion.lower() == "registro":
    print("\nAccion de registro")
    name = str(input("Ingresa el nombre: "))
    last_name = str(input("Ingresa tus apellidos: "))
    email = str(input("Ingresa tu email: "))
    password = str(input("Ingresa tu contraseña: "))


elif accion.lower() == "login":
    print("\nAccion de login")
    email = str(input("Ingresa tu email: "))
    password = str(input("Ingresa tu contraseña: "))
