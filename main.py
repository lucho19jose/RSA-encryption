import tkinter
from tkinter import *
from tkinter import ttk
from vistas.navegador import *


if __name__ == '__main__':
    ventana = Tk()
    ventana.geometry("420x400")
    ventana.resizable(width=False, height=False)
    app = Aplication(ventana)

    ventana.mainloop()
