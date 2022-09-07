class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def calificacion(self):
        if float(self.nota) > 3:
            print("Su calificación de 1 a 5 es: ",self.nota,", significa que: Aprobo el curso")
        else:
            print("Su calificación de 1 a 5 es: ",self.nota, ", significa que: No aprobo el curso")
        return

alum1 = Alumno("Andrea Muñoz", "3.5")
print(alum1.nombre)
print(alum1.nota)
alum1.calificacion()


