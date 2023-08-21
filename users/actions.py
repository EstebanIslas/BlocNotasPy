import users.user as model
import notas.actions as notaController

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

        try:
            email = str(input("\n\nIngresa tu email: "))
            password = str(input("Ingresa tu contraseña: "))

            user = model.User('', '', email, password)

            login = user.identificar()

            if email == login[3]:
                print(f"\n\nBienvenido {login[1]} a Tus Notas\n")
                self.menuActions(login)

        except Exception as e:
            print(f"Acceso Denegado!!")
        
    def menuActions(self, user_log):
        print("""
        Menu de acciones:
        - Crear nota    (crear)
        - Mostrar nota  (mostrar)
        - Eliminar Nota (eliminar)
        - Cerrar Sesion (salir)
        """)

        action = str(input("Selecciona la accion a realizar: "))
        nota_controller = notaController.Actions()

        if action.lower() == "crear":
            nota_controller.crear(user_log)
            self.menuActions(user_log)

        elif action.lower() == "mostrar":
            
            nota_controller.mostrar(user_log)
            self.menuActions(user_log)

        elif action.lower() == "eliminar":
            nota_controller.eliminar(user_log)
            self.menuActions(user_log)

        elif action.lower() == "salir":
            print("Sesión Finalizada!! :)")
            exit()
