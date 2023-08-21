from users import actions


print("""
Acciones Disponibles:
    - Registro
    - Login
""")

doThe = actions.Actions() #Instancia de clase users

accion = str(input("Ingresa el comando que desee utilizar:"))

if accion.lower() == "registro":
    doThe.register()

elif accion.lower() == "login":
    doThe.login()
