import users.user as model

class Actions():
    
    def register(self):
        name = str(input("\n\nIngresa el nombre: "))
        last_name = str(input("Ingresa tus apellidos: "))
        email = str(input("Ingresa tu email: "))
        password = str(input("Ingresa tu contraseña: "))

        user = model.User(name, last_name, email, password)
        registro = user.register()

        if registro[0] >= 1:
            print(f"\nCreación de {registro[1].name} realizado con exito!!")
        else:
            print("Fallo en el registro!!")

    def login(self):
        email = str(input("Ingresa tu email: "))
        password = str(input("Ingresa tu contraseña: "))
    