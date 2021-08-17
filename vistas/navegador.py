import tkinter
from tkinter import *
from tkinter import ttk
from vistas.file import *


class Aplication(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ventana = ventana

        self.ventana.title("RSA System")
        self.ventana.iconbitmap("img/key.ico")

        # Contenedor de Paneles

        # declarando para crear los navegadores
        self.navegador = ttk.Notebook(self)

        # Panel de Inicio
        self.inicio = Label(
            self.navegador, text="Welcome/Bienvenido a RSA sys")
        self.author = Label(
            self.navegador, text="By: jose, Course: Seguridad Informatica, EPIS")
        self.navegador.add(self.inicio, text="Inicio")

        # mainFile
        self.main = MainFile(self.navegador)
        self.navegador.add(self.main, text="RSA Algorithm")

        self.navegador.add(self.author, text="about")
        self.navegador.pack()
        self.pack()
