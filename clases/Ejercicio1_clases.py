class Vehiculo:
    color = "Azul"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self):
        self.velocidad = "50km/h"
        self.cilindrada = "6 litros"


persona1 = Coche()
print("\n COCHE \n Color: ",persona1.color,"\n Cantidad ruedas: ",persona1.ruedas,"\n Cantidad de puertas: ",persona1.puertas)
print(" Cilindrada: ",persona1.cilindrada, "\n Velocidad: ",persona1.velocidad)