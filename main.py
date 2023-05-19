import psycopg2

#Para establecer la conexión creamos un objeto
connection = psycopg2.connect(
    #Acá recibe unos parametros 
    host="localhost",
    user="postgres",
    password="1234",
    database="personas",
    port="5432"
)

connection.autocommit = True

#Creamos un tabla
def crearTabla(): #Función para crear una tabla
    cursor = connection.cursor() #Ejecuta todas las querys en la BD
    query ="CREATE TABLE usuario(id numeric(10), nombre varchar(30),telefono numeric(10))"
    try:
        cursor.execute(query)
    except:
        print("La tabla usuario ya existe")
    cursor.close()

#Función para insertar datos
def insertarDatos():
    cursor = connection.cursor()
    query = """ INSERT INTO usuario (id,nombre,telefono) values (0001,'Fabian','12345678')"""
    cursor.execute(query)
    cursor.close()

#Función para actualizar datos
def actualizarDato():
    cursor = connection.cursor()
    query = """ UPDATE usuario set nombre='Angie' where nombre='Fabian'"""
    cursor.execute(query)
    cursor.close()

#crearTabla()
#insertarDatos()
actualizarDato()