from cmath import pi


def areaTriangulo(altura, base):
    return (altura*base)/2

def areaCirculo(radio=5):
    return float(pi*radio**2)

areaT=areaTriangulo(4,8)
print(areaT)
areaC=areaCirculo()
print(areaC)