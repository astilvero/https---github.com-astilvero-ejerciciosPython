from functools import reduce

lista=list(range(40))

def info(n):
    if n % 2:
        return True
    else:
        return False

respuesta=list(filter(info, lista))
print(respuesta)
respuestaAdd=reduce((lambda x,y: x+y),respuesta)
print(respuestaAdd)