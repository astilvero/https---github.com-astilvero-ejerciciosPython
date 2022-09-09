# crear un archivo py y dentro crearéis una clase Vehículo, haréis un 
# objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:

    def __init__(self, llantas, color, marca):
        self.llantas=llantas
        self.color=color
        self.marca=marca

    def __str__(self):
        return f'El carro es de marca {self.marca} de color {self.color} y tiene {self.llantas} llantas '

auto=Vehiculo("4","azul","audi")
print(auto)

f=open('vehiculo_guardado.bin','wb')
pickle.dump(auto,f)
f.close()

f=open('vehiculo_guardado.bin','rb')
vehiculo_cargado=pickle.load(f)

print(vehiculo_cargado)
f.close()


