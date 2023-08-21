import notas.nota as model

class Actions:

    def crear(self, usuario):
        print(f"\n{usuario[1]} Crea una nota nueva!")
        title = str(input("Introduce el titulo de la nota: "))
        description = str(input("Introduce el contenido de la nota: "))

        nota = model.Nota(usuario[0], title, description)
        save = nota.save()

        if save[0] >= 1:
            print(f"\nLa nota {nota.title} se ha creado con éxito!!")

        else:
            print(f"\nError: La nota no se ha creado")

    def mostrar(self, usuario):
        print(f"{usuario[1]} estas son tus notas\n")

        nota = model.Nota(usuario[0])
        notas = nota.show()

        #Recorrer notas
        for nota in notas:
            print("*********************************")
            print(nota[2])
            print(nota[3])
            print(nota[4])
            print("*********************************")
    