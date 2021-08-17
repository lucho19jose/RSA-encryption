import tkinter
from tkinter import *
from tkinter import ttk
from vistas.frame_rsa import *
from vistas.file import *


class Aplication(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ventana = ventana

        self.ventana.title("RSA System")
        self.ventana.iconbitmap("img/corona.ico")

        # Contenedor de Paneles

        # declarando para crear los navegadores
        self.navegador = ttk.Notebook(self)

        # Panel de Inicio
        self.inicio = Label(
            self.navegador, text="Welcome/Bienvenido a RSA sys")
        self.author = Label(self.navegador, text="by: jose")
        self.navegador.add(self.inicio, text="Inicio")
        self.navegador.add(self.author, text="Inicio")

        # panel de estudiante
        self.RSA = RSAview(self.navegador)
        self.navegador.add(self.RSA, text="what")

        # mainFile
        self.main = MainFile(self.navegador)
        self.navegador.add(self.main, text="RSA")

        self.navegador.pack()
        self.pack()
