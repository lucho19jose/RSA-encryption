from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *
import random


class RSAview(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def mcd(a, b):
            '''Calcula el maximo comun divisor de dos numeros a y b'''
            a = int(a)
            b = int(b)
            while a:
                a, b = b % a, a
            self.entry_mcd.delete(0, END)
            self.entry_mcd.insert(0, b)
    
        # label Title
        self.label_title_MCD = Label(self, text="Compute MCD")
        self.label_title_MCD.grid(
            row=0, column=0, columnspan=2, pady=10, padx=10)

        # Label num 1
        self.label_num1 = Label(self, text="Num 1:")
        self.label_num1.grid(row=1, column=0, pady=10, padx=10)

        self.entry_num1 = Entry(self, state='normal')
        self.entry_num1.grid(row=1, column=1, pady=10, padx=10)

        # Label num 2
        self.label_num2 = Label(self, text="Num 2:")
        self.label_num2.grid(row=2, column=0, pady=10, padx=10)

        self.entry_num2 = Entry(self, state='normal')
        self.entry_num2.grid(row=2, column=1, pady=10, padx=10)

        # Button compute
        self.button_compute = Button(self, text="Compute MCD", command=lambda: mcd(
            self.entry_num1.get(), self.entry_num2.get()))
        self.button_compute.grid(row=3, column=1, pady=10, padx=10)

        # Label num 3
        self.label_MCD = Label(self, text="MCD:")
        self.label_MCD.grid(row=4, column=0, pady=10, padx=10)

        self.entry_mcd = Entry(self, state='normal')
        self.entry_mcd.grid(row=4, column=1, pady=10, padx=10)
