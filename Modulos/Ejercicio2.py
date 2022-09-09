import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Es hora de salir del trabajo")
else:
    print("Faltan ",18-int(hora),"horas",59-int(minutos),"minutos")

    #print({} {}.format(18-int(hora),59-int(minutos)))