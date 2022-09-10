#crear una lista de RadioButton que muestre la opción que se ha seleccionado y 
# que contenga un botón de reinicio para que deje todo como al principio.

from tkinter import *

window=Tk()

def mostrar():
    m.config(text='{}'.format(seleccion.get()))

def reiniciar():
    seleccion.set(None)
    m.config(text="")
    
seleccion=StringVar()
seleccion.set(None)

Radiobutton(window, text='TI', value='T.I.', variable=seleccion, command=mostrar).pack(anchor='w')
Radiobutton(window, text='Cedula', value='Cedula', variable=seleccion, command=mostrar).pack(anchor='w')
Radiobutton(window, text='Pasaporte', value='Pasaporte', variable=seleccion, command=mostrar).pack(anchor='w')

m=Label(window)
m.pack()

Button(window, text='reestablecer', command=reiniciar).pack()

window.mainloop()