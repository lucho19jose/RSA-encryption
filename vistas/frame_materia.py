from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class VistaMateria(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		def nuevo():
			self.entry_nombre.config(state="normal")
			self.entry_creditos.config(state="normal")

		def agregar_datos():

			query = 'INSERT INTO materia VALUES (NULL, ?, ?)'
			parametros = (self.entry_nombre.get(), self.entry_creditos.get())

			conn = Conectar_db()
			conn.run_db(query, parametros)
			#limpiar campos
			self.entry_nombre.delete(0, END)
			self.entry_creditos.delete(0, END)

			#actualiza la tabla
			listar_datos()

		def eliminar_datos():

			codigo = self.tabla.item(self.tabla.selection())['text']
			query = 'DELETE FROM materia WHERE codigo_m = ?'

			conn = Conectar_db()
			conn.run_db(query, (codigo,))
			#actualiza la tabla
			listar_datos()

		def actualizar_datos(codigo_n, codigo_a, nombre_n, nombre_a, credito_n, credito_a):
			query = 'UPDATE materia SET codigo_m = ?, nombre_m = ?, creditos_m = ? WHERE codigo_m = ? AND nombre_m = ? AND creditos_m = ?'
			parametros = (codigo_n, nombre_n, credito_n, codigo_a, nombre_a, credito_a)

			conn = Conectar_db()
			conn.run_db(query, parametros)
			self.ventana_editar.destroy()
			listar_datos()


		self.label_titulo_materia = Label(self, text="Registrar Nueva Materia")
		self.label_titulo_materia.grid(row = 0, column = 0, columnspan = 2)#posicionando y empaquetando 

		#Campo de Nombre de la materia
		self.label_nombre_carrera = Label(self, text = "Nombre Materia: ")
		self.label_nombre_carrera.grid(row = 1, column = 0, pady = 10, padx = 10)

		self.entry_nombre = Entry(self, state = 'readonly')
		self.entry_nombre.grid(row = 1, column = 1, pady = 10, padx = 10)

		#Campo de Duracion de la materia
		self.label_creditos = Label(self, text = "Creditos de la materia: ")
		self.label_creditos.grid(row = 2, column = 0, pady = 10, padx = 10)

		self.entry_creditos = Entry(self, state = 'readonly')
		self.entry_creditos.grid(row = 2, column = 1, pady = 10, padx = 10)

		#Boton Nuevo
		self.boton_nuevo = Button(self, text = "Registrar Nueva Materia", command= nuevo)
		self.boton_nuevo.grid(row=3, column=0, pady = 10, padx = 10)

		#Boton Guardar
		self.boton_guardar = Button(self, text = "Guardar Materia", command = agregar_datos)
		self.boton_guardar.grid(row=3, column=1, pady = 10, padx = 10)

		#tabla

		self.tabla = ttk.Treeview(self, columns = ('',' '))
		self.tabla.grid(row = 5, column = 0, columnspan=3, pady = 10, padx = 10)
		self.tabla.heading('#0', text = "Codigo de Materia")
		self.tabla.heading('#1', text = "Nombre de Materia")
		self.tabla.heading('#2', text = "Duracion de Materia")

		#Boton Eliminar
		self.boton_eliminar = Button(self, text = "Eliminar Materia", command = eliminar_datos)
		self.boton_eliminar.grid(row=8, column=1, pady = 10, padx = 10)		

		def editar_datos():

			codigo = self.tabla.item(self.tabla.selection())['text']
			nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
			creditos_anti = self.tabla.item(self.tabla.selection())['values'][1]

			self.ventana_editar = Toplevel()
			self.ventana_editar.title("Editar Materia")

			#Label y Campo de nombre
			self.label_nombre_antiguo = Label(self.ventana_editar, text = "Nombre de Materia Antigua: ")
			self.label_nombre_antiguo.grid(row = 1, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_anti), state = 'readonly')
			self.entry_nombre_antiguo.grid(row = 1, column = 1, pady = 10, padx = 10)

			self.label_nombre_nuevo = Label(self.ventana_editar, text = "Nombre de la Nueva Materia : ")
			self.label_nombre_nuevo.grid(row = 2, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_nuevo = Entry(self.ventana_editar)
			self.entry_nombre_nuevo.grid(row = 2, column = 1, pady = 10, padx = 10)
	
	
			#Label y campo de duracion
			self.label_creditos_antigua = Label(self.ventana_editar, text = "Creditos Antigua: ")
			self.label_creditos_antigua.grid(row = 3, column = 0, pady = 10, padx = 10)
	
	
			self.entry_creditos_antigua = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = creditos_anti), state = 'readonly')
			self.entry_creditos_antigua.grid(row = 3, column = 1, pady = 10, padx = 10)

			self.label_creditos_nuevo = Label(self.ventana_editar, text = "Creditos Nueva: ")
			self.label_creditos_nuevo.grid(row = 4, column = 0, pady = 10, padx = 10)
	
	
			self.entry_creditos_nuevo = Entry(self.ventana_editar)
			self.entry_creditos_nuevo.grid(row = 4, column = 1, pady = 10, padx = 10)

			#Boton Actualizar
			self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar Materia", command = lambda: actualizar_datos(codigo, codigo,
			self.entry_nombre_nuevo.get(), nombre_anti, self.entry_creditos_nuevo.get(), creditos_anti))
			self.boton_actualizar.grid(row=5, column=0,columnspan = 2, pady = 10, padx = 10)


		#Boton Editar
		self.boton_editar = Button(self, text = "Editar Materia", command=editar_datos)
		self.boton_editar.grid(row=8, column=0, pady = 10, padx = 10)


		#listar Datos

		def listar_datos():

			#Eliminar datos de la tabla
			recorrer_tabla = self.tabla.get_children()
			for elementos in recorrer_tabla:
				self.tabla.delete(elementos)

			query = "SELECT * FROM materia"
			conn = Conectar_db()
			datos = conn.run_db(query)

			for materia in datos:
				self.tabla.insert('',1,text = materia[0], value = (materia[1],materia[2]))


		listar_datos()