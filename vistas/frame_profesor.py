import tkinter 
from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class VistaProfesor(ttk.Frame):
	"""docstring for VistaProfesor"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		def nuevo():
			self.entry_nombre.config(state="normal")
			self.entry_telefono.config(state="normal")
			self.entry_direccion.config(state="normal")

		def agregar_datos():

			query = 'INSERT INTO profesor VALUES (NULL, ?, ?, ?)'
			parametros = (self.entry_nombre.get(), self.entry_telefono.get(), self.entry_direccion.get())

			conn = Conectar_db()
			conn.run_db(query, parametros)
			#limpiar campos
			self.entry_nombre.delete(0, END)
			self.entry_telefono.delete(0, END)
			self.entry_direccion.delete(0, END)
			#actualiza la tabla
			listar_datos()

		def eliminar_datos():

			codigo = self.tabla.item(self.tabla.selection())['text']
			query = 'DELETE FROM profesor WHERE codigo_p = ?'

			conn = Conectar_db()
			conn.run_db(query, (codigo,))
			#actualiza la tabla
			listar_datos()

		def actualizar_datos(nombre_n, nombre_a, telefono_n, telefono_a, direccion_n, direccion_a):

			#En este caso estamos actucalizando usando el telefono but not the id
			query = "UPDATE profesor SET nombre_p = ?, telefono_p = ?, direccion_p = ? WHERE telefono_p = ?"
			parametros = (nombre_n, telefono_n, direccion_n, telefono_a)

			conn = Conectar_db()
			conn.run_db(query, parametros)
			self.ventana_editar.destroy()
			listar_datos()


		self.label_titulo_profesor = Label(self, text="Registro de Docentes")
		self.label_titulo_profesor.grid(row=0, column=1, pady = 10, padx = 10)


		#campo de nombre de profesor
		self.nombre_profesor = Label(self, text = "Nombre de Profesor: ")
		self.nombre_profesor.grid(row = 1, column = 0,pady = 10, padx = 10)

		self.entry_nombre = Entry(self, state='readonly')
		self.entry_nombre.grid(row = 1, column = 1,pady = 10, padx = 10)

		#Campo de Telefono Profesor
		self.telefono_profesor = Label(self, text = "Telefono de Profesor: ")
		self.telefono_profesor.grid(row = 2, column = 0,pady = 10, padx = 10)

		self.entry_telefono = Entry(self, state='readonly')
		self.entry_telefono.grid(row = 2, column = 1,pady = 10, padx = 10)

		#Direccion de Profesor
		self.direccion_profesor = Label(self, text = "Direccion de Profesor: ")
		self.direccion_profesor.grid(row = 3, column = 0,pady = 10, padx = 10)

		self.entry_direccion = Entry(self, state='readonly')
		self.entry_direccion.grid(row = 3, column = 1,pady = 10, padx = 10)

		#Nuevo Profesor
		self.boton_registrar = Button(self, text="Registrar Nuevo Profesor", command = nuevo)
		self.boton_registrar.grid(row = 4, column = 0,pady = 10, padx = 10)

		#Guardar Profesor
		self.boton_guardar = Button(self, text="Guardar Profesor", command = agregar_datos)
		self.boton_guardar.grid(row = 4, column = 1,pady = 10, padx = 10)

		#tabla para mostrar
		self.tabla = ttk.Treeview(self, columns = ('',' ',' '))
		self.tabla.grid(row = 5, column = 0, columnspan=3, pady = 10, padx = 10)
		self.tabla.heading('#0', text = "Codigo de Profesor")
		self.tabla.heading('#1', text = "Nombre de Profesor")
		self.tabla.heading('#2', text = "Telefono de Profesor")
		self.tabla.heading('#3', text = "Direccion de Profesor")


		def editar_datos():

			nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]		
			telefono_anti = self.tabla.item(self.tabla.selection())['values'][1]
			direccion_anti = self.tabla.item(self.tabla.selection())['values'][2]

			self.ventana_editar = Toplevel()
			self.ventana_editar.title("Editar Carrera")

			#Label y Campo de nombre
			self.label_nombre_antiguo = Label(self.ventana_editar, text = "Nombre del Profesor: ")
			self.label_nombre_antiguo.grid(row = 1, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_anti), state = 'readonly')
			self.entry_nombre_antiguo.grid(row = 1, column = 1, pady = 10, padx = 10)

			self.label_nombre_nuevo = Label(self.ventana_editar, text = "Nombre de Profesor nuevo: ")
			self.label_nombre_nuevo.grid(row = 2, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_nuevo = Entry(self.ventana_editar)
			self.entry_nombre_nuevo.grid(row = 2, column = 1, pady = 10, padx = 10)
	
	
			#Label y capo de telefono
			self.label_telefono_antigua = Label(self.ventana_editar, text = "Telefono Antiguo: ")
			self.label_telefono_antigua.grid(row = 3, column = 0, pady = 10, padx = 10)
	
			self.entry_telefono_antigua = Entry(self.ventana_editar, textvariable= StringVar(self.ventana_editar, value = telefono_anti), state = 'readonly')
			self.entry_telefono_antigua.grid(row = 3, column = 1, pady = 10, padx = 10)



			self.label_telefono_nuevo = Label(self.ventana_editar, text = "Nuevo Telefono: ")
			self.label_telefono_nuevo.grid(row = 4, column = 0, pady = 10, padx = 10)
	
			self.entry_telefono_nuevo = Entry(self.ventana_editar)
			self.entry_telefono_nuevo.grid(row = 4, column = 1, pady = 10, padx = 10)


			#La direccion del Profesor
			self.label_direccion_antigua = Label(self.ventana_editar, text = "Direccion Antigua: ")
			self.label_direccion_antigua.grid(row = 5, column = 0, pady = 10, padx = 10)
	
			self.entry_direccion_antigua = Entry(self.ventana_editar,textvariable = StringVar(self.ventana_editar, value = direccion_anti), state = 'readonly')
			self.entry_direccion_antigua.grid(row = 5, column = 1, pady = 10, padx = 10)



			self.label_direccion_nuevo = Label(self.ventana_editar, text = "Direccion  Nueva: ")
			self.label_direccion_nuevo.grid(row = 6, column = 0, pady = 10, padx = 10)
	
			self.entry_direccion_nuevo = Entry(self.ventana_editar)
			self.entry_direccion_nuevo.grid(row = 6, column = 1, pady = 10, padx = 10)


			#Boton Actualizar
			self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar Profesor", command = lambda: actualizar_datos(self.entry_nombre_nuevo.get(), nombre_anti,
				self.entry_telefono_nuevo.get(), telefono_anti, self.entry_direccion_nuevo.get(), direccion_anti))
			self.boton_actualizar.grid(row=7, column=0,columnspan = 2, pady = 10, padx = 10)


		#Boton Editar
		self.boton_editar = Button(self, text = "Editar Profesor", command=editar_datos)
		self.boton_editar.grid(row=6, column=0, pady = 10, padx = 10)

		#Boton Eliminar
		self.boton_eliminar = Button(self, text = "Eliminar Profesor", command = eliminar_datos)
		self.boton_eliminar.grid(row=6, column=1, pady = 10, padx = 10)

		#listar Datos

		def listar_datos():

			#Eliminar datos de la tabla
			recorrer_tabla = self.tabla.get_children()
			for elementos in recorrer_tabla:
				self.tabla.delete(elementos)

			query = "SELECT * FROM profesor"
			conn = Conectar_db()
			datos = conn.run_db(query)

			for profesor in datos:
				self.tabla.insert('',1,text = profesor[0], value = (profesor[1],profesor[2],profesor[3]))


		listar_datos()

