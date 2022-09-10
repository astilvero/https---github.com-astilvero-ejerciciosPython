#crear una lista de RadioButton que muestre la opción que se ha seleccionado y 
# que contenga un botón de reinicio para que deje todo como al principio.

import tkinter
from tkinter import ttk

window=tkinter.Tk()

def reiniciar(event):
    print('reestrablecido')

seleccion=tkinter.StringVar()

rad1=ttk.Radiobutton(window, text='TI', value='1', variable=seleccion)
rad2=ttk.Radiobutton(window, text='Cedula', value='2', variable=seleccion)
rad3=ttk.Radiobutton(window, text='Pasaporte', value='3', variable=seleccion)

rad1.grid(column=0, row=1, padx=3, pady=3)
rad2.grid(column=0, row=2, padx=3, pady=3)
rad3.grid(column=0, row=3, padx=3, pady=3)

boton=tkinter.Button(window, text='reestablecer')
boton.pack()

boton.bind('<Button-1>', reiniciar)

window.mainloop()