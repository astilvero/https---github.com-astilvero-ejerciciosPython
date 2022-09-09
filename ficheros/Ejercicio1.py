#Crear un archivo py donde creeis un archivo txt, lo abrais y 
# escribas dentro del archivo.

f=open('archivo.txt','w')
cadena="Atención esto es un fichero y va a ser creado"
f.writelines(cadena)
f.close()
