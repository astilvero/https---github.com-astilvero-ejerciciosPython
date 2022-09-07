class Alumno:
    
    def iniciar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def calificacion(self):
        if float(self.nota) > 3:
            print("Su calificación de 1 a 5 es: ",self.nota,", significa que: Aprobo el curso")
        else:
            print("Su calificación de 1 a 5 es: ",self.nota, ", significa que: No aprobo el curso")
        

alum1 = Alumno()

alum1.iniciar("Andrea Muñoz", "4.5")

alum1.imprimir()
alum1.calificacion()


