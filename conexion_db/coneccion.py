import sqlite3

conexion = sqlite3.connect("../db/base_de_datos.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM carrera")

carreras = cursor.fetchall()

for carrera in carreras:
	print(carrera)


conexion.close()