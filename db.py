import sqlite3
from sqlite3 import Error
conexion = ''
def get_db():
    try:
        conexion = sqlite3.connect('database/database')
        return conexion
    except Error:
        print(Error)

def close_db():
    conexion.close()

def actualizarusuario(id,nombre,usuario,correo,contraseña,fecha,tipoDeDocumento,celular,departamento,ciudad):
    conexion = get_db()
    cursor = conexion.cursor()
    strsql = "UPDATE usuario SET (id,nombre,usuario,correo,contraseña,fecha,tipoDeDocumento,celular,departamento,ciudad) = ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}') WHERE id = {}".format(id,nombre,usuario,correo,contraseña,fecha,tipoDeDocumento,celular,departamento,ciudad,id)
    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def consultardatos(usuario):
    conexion = get_db()
    cursor = conexion.cursor()
    strsql = "SELECT * FROM usuario WHERE usuario = '{}'".format(usuario)
    cursor.execute(strsql)
    conexion.commit()
    datos = cursor.fetchall()
    print(datos)

def obtener_conexion():
    try:
        conn = sqlite3.connect('database/db_peliculas.db')
        return conn
    except Error:
        print(Error)


def agregar_pelicula(nombre, duracion, director, genero, sinopsis, caratula):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql=""" INSERT INTO peliculas(nombre, duracion, director, genero, sinopsis, caratula) 
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(nombre, duracion, director, genero, sinopsis, caratula)
    
    cursor.execute(sql)
    conn.commit()
    conn.close()

def agregar_funcion(sala, hora, capacidad, pelicula):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql=""" INSERT INTO funciones(sala, hora, capacidad, pelicula) 
    VALUES ({}, '{}', {}, '{}')""".format(sala, hora, capacidad, pelicula)
    
    cursor.execute(sql)
    conn.commit()
    conn.close()

def mostrar_tabla(tabla):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """ SELECT * FROM {}""".format(tabla)
    
    cursor.execute(sql)

    datos=cursor.fetchall()
    conn.close()    

    return datos

def elminar_dato(tabla, n):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql1 = """ PRAGMA foreign_keys = ON"""
    sql2 = """DELETE FROM {} WHERE {}""".format(tabla, n)
    
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
    conn.close()    

def editar_dato(tabla,s,h,c,p):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """ UPDATE {} SET {},{},{},{} WHERE {}""".format(tabla,s,h,c,p,p)
    
    cursor.execute(sql)
    conn.commit()
    conn.close()    



def contar_dato(tabla,n):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """SELECT COUNT(*) FROM {} WHERE id ={}""".format(tabla,n)

    cursor.execute(sql)

    contar=cursor.fetchall()
    conn.close()  
    return contar


def consultar_dato(tabla,n):
    conn = obtener_conexion()
    Cursor = conn.cursor()

    sql=""" SELECT * FROM {} WHERE {}""".format(tabla, n)

    Cursor.execute(sql)
    valor = Cursor.fetchall()
    conn.close()
    
    return valor

