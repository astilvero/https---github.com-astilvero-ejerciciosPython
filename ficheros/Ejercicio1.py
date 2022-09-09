#Crear un archivo py donde creeis un archivo txt, lo abrais y 
# escribas dentro del archivo.

f=open('archivo.txt','w')
cadena="Atención esto es un fichero y va a ser creado"
f.writelines(cadena)
f.close()

f=open('archivo.txt','r+')
f.readline()
f.writelines(", Atención este fichero ya se creo y se ha modificado")

f.seek(0)
print(f.read())
f.close()