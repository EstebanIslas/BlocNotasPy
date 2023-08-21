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
            