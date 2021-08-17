from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class Vista_carrera(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		def nuevo():
			self.entry_nombre.config(state="normal")
			self.entry_duracion.config(state="normal")



		def nueva_carrera():

			self.entry_nombre.config(state = "normal")
			self.entry_duracion.config(state = "normal")

		def agregar_datos():

			query = 'INSERT INTO carrera VALUES (NULL, ?, ?)'
			parametros = (self.entry_nombre.get(), self.entry_duracion.get())

			conn = Conectar_db()
			conn.run_db(query, parametros)
			#limpiar campos
			self.entry_nombre.delete(0, END)
			self.entry_duracion.delete(0, END)

			#actualiza la tabla
			listar_datos()

		def eliminar_datos():

			codigo = self.tabla.item(self.tabla.selection())['text']
			query = 'DELETE FROM carrera WHERE codigo_c = ?'

			conn = Conectar_db()
			conn.run_db(query, (codigo,))
			#actualiza la tabla
			listar_datos()

		#Actualiza Datos
		def actualizar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_anti, duracion_nueva, duracion_anti):
			query = 'UPDATE carrera SET codigo_c = ?, nombre_c = ?, duracion_c = ? WHERE codigo_c = ? AND nombre_c = ? AND duracion_c = ?'
			parametros = (codigo_n, nombre_nuevo ,duracion_nueva, codigo_a, nombre_anti, duracion_anti)

			conn = Conectar_db()
			conn.run_db(query, parametros)
			self.ventana_editar.destroy()

			#Actualizar Tabla
			listar_datos()

		#label titulo de Registrar
		self.label_titulo_registrar = Label(self, text="Registrar Nueva Carrera")
		self.label_titulo_registrar.grid(row = 0, column = 0, columnspan = 2, pady = 10, padx=10)#posicionando y empaquetando 

		#Label y Campo de nombre
		self.label_nombre = Label(self, text = "Nombre de Carrera: ")
		self.label_nombre.grid(row = 1, column = 0, pady = 10, padx = 10)

		self.entry_nombre = Entry(self, state = 'readonly')
		self.entry_nombre.grid(row = 1, column = 1, pady = 10, padx = 10)


		#Label y campo de duracion
		self.label_duracion = Label(self, text = "Duracion de Carrera: ")
		self.label_duracion.grid(row = 2, column = 0, pady = 10, padx = 10)


		self.entry_duracion = Entry(self, state = 'readonly')
		self.entry_duracion.grid(row = 2, column = 1, pady = 10, padx = 10)


		#Boton Nuevo
		self.boton_nuevo = Button(self, text = "Nuevo", command= nuevo)
		self.boton_nuevo.grid(row=3, column=0, pady = 10, padx = 10)

		#Boton Guardar
		self.boton_guardar = Button(self, text = "Guardar",command = agregar_datos)
		self.boton_guardar.grid(row=3, column=1, pady = 10, padx = 10)


		self.label_titulo_lista = Label(self, text="Lista de Carreras")
		self.label_titulo_lista.grid(row = 4, column = 0, columnspan = 2)#posicionando y empaquetando 

		#tabla

		self.tabla = ttk.Treeview(self, columns = ('',' '))
		self.tabla.grid(row = 5, column = 0, columnspan=3, pady = 10, padx = 10)
		self.tabla.heading('#0', text = "Codigo de Carrera")
		self.tabla.heading('#1', text = "Nombre de Carrera")
		self.tabla.heading('#2', text = "Duracion de la carrera")


		#Boton Eliminar
		self.boton_eliminar = Button(self, text = "Eliminar Carrera", command = eliminar_datos)
		self.boton_eliminar.grid(row=6, column=0, pady = 10, padx = 10)

		def editar_datos():

			codigo = self.tabla.item(self.tabla.selection())['text']
			nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
			duracion_anti = self.tabla.item(self.tabla.selection())['values'][1]

			self.ventana_editar = Toplevel()
			self.ventana_editar.title("Editar Carrera")

			#Label y Campo de Codigo en la emergente
			self.label_codigo = Label(self.ventana_editar, text = "Codigo de Carrera: ")
			self.label_codigo.grid(row = 0, column = 0, pady = 10, padx = 10)
	
			self.entry_codigo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo), state = 'readonly')
			self.entry_codigo.grid(row = 0, column = 1, pady = 10, padx = 10)

			#Label y Campo de nombre
			self.label_nombre_antiguo = Label(self.ventana_editar, text = "Nombre de Carrera: ")
			self.label_nombre_antiguo.grid(row = 1, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_anti), state = 'readonly')
			self.entry_nombre_antiguo.grid(row = 1, column = 1, pady = 10, padx = 10)

			self.label_nombre_nuevo = Label(self.ventana_editar, text = "Nombre de Carrera: ")
			self.label_nombre_nuevo.grid(row = 2, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_nuevo = Entry(self.ventana_editar)
			self.entry_nombre_nuevo.grid(row = 2, column = 1, pady = 10, padx = 10)
	
	
			#Label y campo de duracion
			self.label_duracion_antigua = Label(self.ventana_editar, text = "Duracion de Carrera Antigua: ")
			self.label_duracion_antigua.grid(row = 3, column = 0, pady = 10, padx = 10)
	
	
			self.entry_duracion_antigua = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = duracion_anti), state = 'readonly')
			self.entry_duracion_antigua.grid(row = 3, column = 1, pady = 10, padx = 10)

			self.label_duracion_nuevo = Label(self.ventana_editar, text = "Duracion de Carrera Nueva: ")
			self.label_duracion_nuevo.grid(row = 4, column = 0, pady = 10, padx = 10)
	
	
			self.entry_duracion_nuevo = Entry(self.ventana_editar)
			self.entry_duracion_nuevo.grid(row = 4, column = 1, pady = 10, padx = 10)

			#Boton Actualizar
			self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar Carrera", command = lambda: actualizar_datos(codigo, codigo, 
			self.entry_nombre_nuevo.get(), nombre_anti, self.entry_duracion_nuevo.get(), duracion_anti))
			self.boton_actualizar.grid(row=5, column=0,columnspan = 2, pady = 10, padx = 10)


		#Boton Editar
		self.boton_editar = Button(self, text = "Editar Carrera", command=editar_datos)
		self.boton_editar.grid(row=6, column=0, columnspan = 2, pady = 10, padx = 10)

		#listar Datos

		def listar_datos():

			#Eliminar datos de la tabla
			recorrer_tabla = self.tabla.get_children()
			for elementos in recorrer_tabla:
				self.tabla.delete(elementos)

			query = "SELECT * FROM carrera"
			conn = Conectar_db()
			datos = conn.run_db(query)

			for carrera in datos:
				self.tabla.insert('',0,text = carrera[0], value = (carrera[1],carrera[2]))

		#Listar datos en la tabla
		listar_datos()




