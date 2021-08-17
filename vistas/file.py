from os import stat
from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *
from tkinter import filedialog as fd
from tkinter import messagebox
from vistas.Algth import generaClaves, cifra, descifra
import random


class MainFile(ttk.Frame):
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

        # to save datas
        self.privateKey = ''
        self.publicKey = ''
        self.FileToEncrypt = ''
        self.FileToDecrypt = ''

        def open_text_file(params):
            # file type
            filetypes = (
                ('text files', '*.txt'),
                ('All files', '*.*')
            )
            # show the open file dialog
            f = fd.askopenfilename(filetypes=filetypes, title="File")
            if f:
                tf = open(f, 'r', encoding="utf8")
                if params == 1:
                    self.FileToEncrypt = tf.read()
                    self.entry_fileToEncrypt.delete(0, END)
                    self.entry_fileToEncrypt.insert(0, f)
                    print(self.FileToEncrypt)
                if params == 2:
                    self.FileToDecrypt = tf.read()
                    self.entry_EncryptedFile.delete(0, END)
                    self.entry_EncryptedFile.insert(0, f)
                    print(self.FileToDecrypt)
                if params == 3:
                    self.publicKey = tf.read()
                    self.entry_publicKey.delete(0, END)
                    self.entry_publicKey.insert(0, f)
                    print(self.publicKey)
                if params == 4:
                    self.privateKey = tf.read()
                    self.entry_PrivateKey.delete(0, END)
                    self.entry_PrivateKey.insert(0, f)
                    print(self.privateKey)
            else:
                print("none to show")

        def getKeys():
            keys = generaClaves(int(self.combo_lengthKey.get()))
            messagebox.showinfo(
                "message", "se han creado las claves con exito")

        def CyperOrDecrypt():
            if self.v.get() == 1:
                if self.entry_fileToEncrypt.get() and self.entry_publicKey.get():
                    print(self.publicKey)
                    cipher = cifra(self.FileToEncrypt, tuple(
                        self.publicKey.replace('(', '').replace(')', '').split(",")))
                    messagebox.showinfo(
                        "message", "texto encriptado con exito")
                    print(cipher)
            else:
                if self.entry_EncryptedFile.get() and self.entry_PrivateKey.get():
                    decrypter = descifra(self.FileToDecrypt.split(" "), tuple(
                        self.privateKey.replace('(', '').replace(')', '').split(",")))
                    messagebox.showinfo(
                        "message", "el texto de ha descifrado con exito")

        def encryptAvailable():
            self.entry_fileToEncrypt.config(state="normal")
            self.entry_publicKey.config(state="normal")
            self.button_OpenFileEncrypt.config(state="normal")
            self.button_OpenFilePK.config(state="normal")

            self.entry_EncryptedFile.delete(0, END)
            self.entry_EncryptedFile.config(state="readonly")
            self.entry_PrivateKey.delete(0, END)
            self.entry_PrivateKey.config(state="readonly")
            self.button_OpenFilePrk.config(state="disabled")
            self.button_OpenFileDecrypt.config(state="disabled")
            self.EncryptDecrypt.config(text="Encrypt File")
            print(self.v.get())

        def decryptAvailable():
            self.entry_fileToEncrypt.delete(0, END)
            self.entry_publicKey.delete(0, END)
            self.entry_fileToEncrypt.config(state="readonly")
            self.entry_publicKey.config(state="readonly")
            self.button_OpenFileEncrypt.config(state="disabled")
            self.button_OpenFilePK.config(state="disabled")

            self.entry_EncryptedFile.config(state="normal")
            self.entry_PrivateKey.config(state="normal")
            self.button_OpenFilePrk.config(state="normal")
            self.button_OpenFileDecrypt.config(state="normal")
            self.EncryptDecrypt.config(text="Decrypt File")
            print(self.v.get())

        # label Title
        self.label_title_file = Label(self, text="File")
        self.label_title_file.grid(
            row=0, column=0, columnspan=2, pady=10, padx=10)

        # generate keys
        self.label_generateKeys = Label(self, text="Generate Keys")
        self.label_generateKeys.grid(row=1, column=0, pady=10, padx=10)

        self.combo_lengthKey = ttk.Combobox(
            self, values=["512", "1024", "2048"], state="readonly")
        self.combo_lengthKey.current(1)
        self.combo_lengthKey.grid(row=1, column=1, pady=0, padx=0)

        self.generateKeys = Button(
            self, text="generate keys", state='normal', command=getKeys)
        self.generateKeys.grid(row=1, column=3, pady=10, padx=5)

        # Label num 1
        self.label_fileToEncrypt = Label(self, text="File to encrypt:")
        self.label_fileToEncrypt.grid(row=2, column=0, pady=10, padx=10)

        self.entry_fileToEncrypt = Entry(self, state='normal')
        self.entry_fileToEncrypt.grid(row=2, column=1, pady=10, padx=10)

        self.button_OpenFileEncrypt = Button(
            self, text=". . .", command=lambda: open_text_file(1))
        self.button_OpenFileEncrypt.grid(row=2, column=2, pady=10, padx=5)

        # Label num 2
        self.label_EncryptedFile = Label(self, text="File to Decrypt:")
        self.label_EncryptedFile.grid(row=3, column=0, pady=10, padx=10)

        self.entry_EncryptedFile = Entry(self, state='readonly')
        self.entry_EncryptedFile.grid(row=3, column=1, pady=10, padx=10)

        self.button_OpenFileDecrypt = Button(
            self, text=". . .", state='disabled', command=lambda: open_text_file(2))
        self.button_OpenFileDecrypt.grid(row=3, column=2, pady=10, padx=5)

        # Label Public Key
        self.label_publicKey = Label(self, text="Public Key:")
        self.label_publicKey.grid(row=4, column=0, pady=10, padx=10)

        self.entry_publicKey = Entry(self, state='normal')
        self.entry_publicKey.grid(row=4, column=1, pady=10, padx=10)

        self.button_OpenFilePK = Button(
            self, text=". . .", command=lambda: open_text_file(3))
        self.button_OpenFilePK.grid(row=4, column=2, pady=10, padx=5)

        # Label Private Key
        self.label_PrivateKey = Label(self, text="Private Key:")
        self.label_PrivateKey.grid(row=5, column=0, pady=10, padx=10)

        self.entry_PrivateKey = Entry(self, state='readonly')
        self.entry_PrivateKey.grid(row=5, column=1, pady=10, padx=10)

        self.button_OpenFilePrk = Button(
            self, text=". . .", state='disabled', command=lambda: open_text_file(4))
        self.button_OpenFilePrk.grid(row=5, column=2, pady=10, padx=5)

        # Label Actions
        self.Label_Actions = Label(self, text="Choose:")
        self.Label_Actions.grid(row=2, column=3, pady=10, padx=10)

        self.v = IntVar()
        self.v.set(1)
        # radio Select
        self.radioButtonChoise = Radiobutton(
            self, text="Encrypt", value=1, variable=self.v, command=encryptAvailable)
        self.radioButtonChoise.grid(row=3, column=3, pady=10, padx=10)

        self.radioButtonChoise = Radiobutton(
            self, text="Decrypt", value=2, variable=self.v, command=decryptAvailable)
        self.radioButtonChoise.grid(row=4, column=3, pady=0, padx=0)

        self.EncryptDecrypt = Button(
            self, text="Encrypt", state='normal', command=CyperOrDecrypt)
        self.EncryptDecrypt.grid(row=6, column=1, pady=10, padx=5)

        # Label generate keys
        """ self.label_MCD = Label(self, text="Generate Keys")
        self.label_MCD.grid(row=4, column=0, pady=10, padx=10)

        self.entry_mcd = Entry(self, state='normal')
        self.entry_mcd.grid(row=4, column=1, pady=10, padx=10) """
