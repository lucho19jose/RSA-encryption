import tkinter 
from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class VistaEstudiante(ttk.Frame):
	"""docstring for VistaEstudiante"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		def nuevo():
			self.entry_nombre.config(state="normal")
			self.entry_telefono.config(state="normal")
			self.entry_edad.config(state="normal")
			self.carre_combo.config(state="normal")

		def agregar_datos():

			carrera = self.carre_combo.get()
			carrera = carrera[0] + carrera[1]

			query = 'INSERT INTO alumno VALUES (NULL, ?, ?, ?, ?)'
			parametros = (self.entry_nombre.get(), self.entry_edad.get(), self.entry_telefono.get(), carrera)

			conn = Conectar_db()
			conn.run_db(query, parametros)
			#limpiar campos
			self.entry_nombre.delete(0, END)
			self.entry_edad.delete(0, END)
			self.entry_telefono.delete(0, END)
			self.carre_combo.delete(0, END)
			#actualiza la tabla
			listar_datos()

		def eliminar_datos():

			codigo = self.tabla.item(self.tabla.selection())['text']
			query = 'DELETE FROM alumno WHERE codigo_a = ?'

			conn = Conectar_db()
			conn.run_db(query, (codigo,))
			#actualiza la tabla
			listar_datos()

		def actualizar_datos(codigo, nombre_n, edad_n, fono_n, carrera_n):

			query = "UPDATE alumno SET nombre_a = ?, edad_a = ?, telefono_a = ?, codigo_c1 = ? WHERE codigo_a = ?"
			parametros = (nombre_n, edad_n, fono_n, carrera_n, codigo)

			conn = Conectar_db()
			conn.run_db(query, parametros)
			self.ventana_editar.destroy()
			listar_datos()
			print(carrera_n)
			

		self.label_titulo_estudiante = Label(self, text="Registrar Nuevo Estudiante")
		self.label_titulo_estudiante.grid(row=0, column=1, columnspan=2)


		#campo de nombre de Estudiante
		self.label_nombre_estudiante = Label(self, text = "Nombre de Estudiante: ")
		self.label_nombre_estudiante.grid(row = 1, column = 0,pady = 10, padx = 10)

		self.entry_nombre = Entry(self, state='readonly')
		self.entry_nombre.grid(row = 1, column = 1,pady = 10, padx = 10)


		#Campo de edad Estudiante
		self.label_edad_estudiante = Label(self, text = "Edad Estudiante: ")
		self.label_edad_estudiante.grid(row = 2, column = 0,pady = 10, padx = 10)

		self.entry_edad = Entry(self, state='readonly')
		self.entry_edad.grid(row = 2, column = 1,pady = 10, padx = 10)


		#Telefono de Estudiante
		self.label_telefono_estudiante = Label(self, text = "Telefono Estudiante: ")
		self.label_telefono_estudiante.grid(row = 3, column = 0,pady = 10, padx = 10)

		self.entry_telefono = Entry(self, state='readonly')
		self.entry_telefono.grid(row = 3, column = 1,pady = 10, padx = 10)

		#intermedia codigo carrera de Estudiante
		self.label_codigo_c_estudiante = Label(self, text = "Carrera Estudiante: ")
		self.label_codigo_c_estudiante.grid(row = 0, column = 2)

		self.carre_combo = ttk.Combobox(self)
		self.carre_combo.grid(row = 1, column = 2, pady = 10, padx = 10)

		def cargar_combo():
			query = 'SELECT codigo_c, nombre_c FROM carrera'
			conn = Conectar_db()
			datos_c = conn.run_db(query)

			for carrera in datos_c:
				values = list(self.carre_combo["values"])
				self.carre_combo["values"] = values + [(carrera[0],',', carrera[1])]

		#Ejecutar cargar Combo
		cargar_combo()

		#Registrar Estudiante Nuevo
		self.boton_registrar = Button(self, text="Registrar Nuevo Estudiante", command = nuevo)
		self.boton_registrar.grid(row = 5, column = 0,pady = 10, padx = 10)


		#Guardar Estudiante
		self.boton_guardar = Button(self, text="Guardar Estudiante", command = agregar_datos)
		self.boton_guardar.grid(row = 5, column = 1,pady = 10, padx = 10)


		#tabla para mostrar
		self.tabla = ttk.Treeview(self, columns = ('','','',''))
		self.tabla.grid(row = 6, column = 0, columnspan=3, pady = 10, padx = 10)
		self.tabla.heading('#0', text = "Codigo del Estudiante")
		self.tabla.heading('#1', text = "Nombre del Estudiante")
		self.tabla.heading('#2', text = "Edad del Estudiante")
		self.tabla.heading('#3', text = "Telefono del Estudiante")
		self.tabla.heading('#4', text = "Carrera")
#		self.tabla.heading('#5', text = "Profesor")
#		self.tabla.heading('#6', text = "Materias")

		def editar_datos():

			codigo = self.tabla.item(self.tabla.selection())['text']
			nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
			edad_anti = self.tabla.item(self.tabla.selection())['values'][1]
			telefono_anti = self.tabla.item(self.tabla.selection())['values'][2]
			carrera_anti = self.tabla.item(self.tabla.selection())['values'][3]

			self.ventana_editar = Toplevel()
			self.ventana_editar.title("Editar Carrera")

			#Label y Campo de nombre
			self.label_nombre_antiguo = Label(self.ventana_editar, text = "Nombre del Estudiante: ")
			self.label_nombre_antiguo.grid(row = 1, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_anti), state = 'readonly')
			self.entry_nombre_antiguo.grid(row = 1, column = 1, pady = 10, padx = 10)

			self.label_nombre_nuevo = Label(self.ventana_editar, text = "Nombre de Estudiante nuevo: ")
			self.label_nombre_nuevo.grid(row = 2, column = 0, pady = 10, padx = 10)
	
			self.entry_nombre_nuevo = Entry(self.ventana_editar)
			self.entry_nombre_nuevo.grid(row = 2, column = 1, pady = 10, padx = 10)
	
	
			#Label y capo de edad
			self.label_edad_antigua = Label(self.ventana_editar, text = "Edad: ")
			self.label_edad_antigua.grid(row = 3, column = 0, pady = 10, padx = 10)
	
			self.entry_edad_antigua = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = edad_anti), state = 'readonly')
			self.entry_edad_antigua.grid(row = 3, column = 1, pady = 10, padx = 10)

			self.label_edad_nuevo = Label(self.ventana_editar, text = "Nueva Edad: ")
			self.label_edad_nuevo.grid(row = 4, column = 0, pady = 10, padx = 10)
	
			self.entry_edad_nuevo = Entry(self.ventana_editar)
			self.entry_edad_nuevo.grid(row = 4, column = 1, pady = 10, padx = 10)


			#La telefono del Estudiante
			self.label_telefono_antigua = Label(self.ventana_editar, text = "Telefono Antiguo: ")
			self.label_telefono_antigua.grid(row = 5, column = 0, pady = 10, padx = 10)
	
			self.entry_telefono_antigua = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = telefono_anti), state = 'readonly')
			self.entry_telefono_antigua.grid(row = 5, column = 1, pady = 10, padx = 10)

			self.label_telefono_nuevo = Label(self.ventana_editar, text = "Telefono  Nuevo: ")
			self.label_telefono_nuevo.grid(row = 6, column = 0, pady = 10, padx = 10)
	
			self.entry_telefono_nuevo = Entry(self.ventana_editar)
			self.entry_telefono_nuevo.grid(row = 6, column = 1, pady = 10, padx = 10)


			#La carrera del Estudiante
			self.label_carrera_antigua = Label(self.ventana_editar, text = "Carrera Antigua: ")
			self.label_carrera_antigua.grid(row = 7, column = 0, pady = 10, padx = 10)
	
			self.entry_carrera_antigua = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = carrera_anti), state = 'readonly')
			self.entry_carrera_antigua.grid(row = 7, column = 1, pady = 10, padx = 10)

			self.label_carrera_nueva = Label(self.ventana_editar, text = "Carrera Nueva: ")
			self.label_carrera_nueva.grid(row = 8, column = 0, pady = 10, padx = 10)

			self.carre_combo = ttk.Combobox(self.ventana_editar)
			self.carre_combo.grid(row = 8, column = 1, pady = 10, padx = 10)
			cargar_combo()


#			carrera = self.carre_combo.get()
#			carrera = carrera[0] + carrera[1]
##			print(carrera)
#			if self.carre_combo.get() == "Select anything":
#				carrera = self.carre_combo.get()
#				carrera = carrera[0] + carrera[1]
#				print(carrera)
			def call_back(object):
				global carrera
				carrera = object
				return carrera

			self.carre_combo.bind("<<ComboboxSelected>>", lambda _ : call_back(self.carre_combo.current()))

			def aSctualizar_datos(codigo, nombre_n, edad_n, fono_n, carrera_n):
				print(carrera_n)

			#Boton Actualizar
			self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar Estudiante", command = lambda: actualizar_datos(codigo, 
			self.entry_nombre_nuevo.get(), self.entry_edad_nuevo.get(), self.entry_telefono_nuevo.get(), call_back(self.carre_combo.current())+1))
			self.boton_actualizar.grid(row=9, column=0,columnspan = 2, pady = 10, padx = 10)


		#Boton modificar
		self.boton_editar = Button(self, text = "Editar Estudiante", command=editar_datos)
		self.boton_editar.grid(row=7, column=0, pady = 10, padx = 10)


		#Boton eliminar
		self.boton_eliminar = Button(self, text = "Eliminar Estudiante", command = eliminar_datos)
		self.boton_eliminar.grid(row=7, column=1, pady = 10, padx = 10)


		#listar Datos

		def listar_datos():

			#Eliminar datos de la tabla
			recorrer_tabla = self.tabla.get_children()
			for elementos in recorrer_tabla:
				self.tabla.delete(elementos)

			query = """SELECT codigo_a, nombre_a, edad_a, telefono_a, nombre_c FROM alumno 
			INNER JOIN carrera ON alumno.codigo_c1 = carrera.codigo_c"""
#			INNER JOIN alumno_profe ON alumno.codigo_a = alumno_profe.codigo_a1 
#			INNER JOIN profesor ON profesor.codigo_p = alumno_profe.codigo_p1
#			INNER JOIN materia_alumno ON alumno.codigo_a = materia_alumno.codigo_a2
#			INNER JOIN materia ON materia.codigo_m = materia_alumno.codigo_m1  
			conn = Conectar_db()
			datos = conn.run_db(query)

			for alumno in datos:
				self.tabla.insert('',1,text = alumno[0], value = (alumno[1],alumno[2],alumno[3],alumno[4]))

		listar_datos()

#query para mostrar todo del alumno
#			query = """SELECT codigo_a, nombre_a, edad_a, telefono_a, nombre_c, nombre_p, nombre_m FROM alumno 
#			INNER JOIN carrera ON alumno.codigo_c1 = carrera.codigo_c 
#			INNER JOIN alumno_profe ON alumno.codigo_a = alumno_profe.codigo_a1 
#			INNER JOIN profesor ON profesor.codigo_p = alumno_profe.codigo_p1
#			INNER JOIN materia_alumno ON alumno.codigo_a = materia_alumno.codigo_a2
#			INNER JOIN materia ON materia.codigo_m = materia_alumno.codigo_m1  """
#		, nombre_p, nombre_m vengo del select lo que hace iner join
