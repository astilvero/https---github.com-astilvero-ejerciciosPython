inicio=int(input("Digite el numero de inicio: "))
fin=int(input("Digite el numero final: "))
num=0

for i in range(inicio,fin):
    if i%2 != 0:
        print(i)
        continue
    num += 1