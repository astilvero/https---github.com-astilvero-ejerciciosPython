# Crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, 
# también debe de tener un label con el texto que queráis.

from tkinter import *

window = Tk()
elem = StringVar()
listBox = Listbox(window)

label=Label(text='Lista de elementos de oficina')
label.pack()

lista=['cuaderno','hojas','computador','grapadora','esferos']
for item in lista:
    listBox.insert(END, item)
listBox.pack()

window.mainloop()