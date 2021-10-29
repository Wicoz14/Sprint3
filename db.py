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
    strsql = "UPDATE usuario SET (id,nombre,correo,contraseña,fecha,tipoDeDocumento,celular,departamento,ciudad) = ('{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}') WHERE usuario = '{}'".format(id,nombre,correo,contraseña,fecha,tipoDeDocumento,celular,departamento,ciudad,usuario)
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
    return datos

def obtener_conexion():
    try:
        conn = sqlite3.connect('database/database')
        return conn
    except Error:
        print(Error)


def agregar_pelicula(nombre, duracion, director, genero,trailer, fechasEstreno,actores, sinopsis, caratula, pancarta):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql=""" INSERT INTO peliculas(nombre, duracion, director, genero, trailer, fechaEstreno, actores, sinopsis, caratula, pancarta) 
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}' )""".format(nombre, duracion, director, genero, trailer, fechasEstreno,actores, sinopsis, caratula, pancarta)
    
    cursor.execute(sql)
    conn.commit()
    conn.close()

def agregar_funcion(pelicula,id_pelicula,formato,fecha,hora,sala,capacidad):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql=""" INSERT INTO funciones(  pelicula,peli_id,formato,fecha, hora,sala, capacidad) 
    VALUES ('{}', {}, '{}','{}','{}', {}, '{}')""".format(pelicula,id_pelicula,formato,fecha,hora,sala,capacidad)
    
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

    sql = """DELETE FROM {} WHERE {}""".format(tabla, n)
    
    cursor.execute(sql)
    conn.commit()
    conn.close()    

def editar_funcion(pelicula,id_pelicula,formato,fecha,hora,sala,capacidad,id_funcion):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """ UPDATE funciones SET {},{},{},{},{},{},{} WHERE {}""".format(pelicula,id_pelicula,formato,fecha,hora,sala,capacidad,id_funcion)
    
    cursor.execute(sql)
    conn.commit()
    conn.close()    

def editar_pelicula(nombre,duracion,director,genero,trailer,estreno,actores,sinopsis,caratula,pancarta,id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """ UPDATE peliculas SET {},{},{},{},{},{},{},{},{},{} WHERE {}""".format(nombre,duracion,director,genero,trailer,estreno,actores,sinopsis,caratula,pancarta,id)
    
    cursor.execute(sql)
    conn.commit()
    conn.close() 


def contar_dato(tabla,n):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = """SELECT COUNT(*) FROM {} WHERE {}""".format(tabla,n)

    cursor.execute(sql)

    contar=cursor.fetchall()
    conn.close()  
    return contar


def consultar_dato(tabla,n,posicion):
    conn = obtener_conexion()
    Cursor = conn.cursor()

    if tabla == "peliculas" :
        if posicion == "ultimo":
            sql =""" SELECT * FROM peliculas ORDER BY peli_id DESC LIMIT 1;"""
        else:
            sql=""" SELECT * FROM {} WHERE {}""".format(tabla, n)
    else:
        sql=""" SELECT * FROM {} WHERE {}""".format(tabla, n)

    Cursor.execute(sql)
    valor = Cursor.fetchall()
    conn.close()
    
    return valor

def retornar_estrenos():
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = "SELECT A.nombre, A.genero, A.director, A.fechaEstreno, A.caratula FROM peliculas A LEFT JOIN funciones B ON A.peli_id = B.peli_id WHERE B.peli_Id IS NULL"

    cursor.execute(sql)

    estrenos=cursor.fetchall()
    conn.close()  
    return estrenos

def retornar_funciones():
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = "SELECT A.nombre, A.genero, A.duracion, A.peli_id, A.caratula FROM peliculas A JOIN funciones B ON A.peli_id = B.peli_id"

    cursor.execute(sql)

    funciones=cursor.fetchall()
    conn.close()  
    return funciones

def retornar_detalle_funcion(id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = "SELECT* FROM peliculas WHERE peli_id={}".format(id)

    cursor.execute(sql)

    funcion=cursor.fetchall()
    conn.close()  
    return funcion

def retornar_busqueda(nombrepelicula):
    conn = obtener_conexion()
    cursor = conn.cursor()

    sql = "SELECT* FROM peliculas WHERE nombre COLLATE SQL_Latin1_General_Cp1_CI_AI LIKE '%{}%'".format(nombrepelicula)

    cursor.execute(sql)

    busqueda=cursor.fetchall()
    conn.close()  
    return busqueda

def consultar_compras(user):
    conexion = get_db()
    cursor = conexion.cursor()
    strsql = "SELECT * FROM tickets WHERE usuario = '{}'".format(user)
    cursor.execute(strsql)
    conexion.commit()
    datoscompras = cursor.fetchall()
    return datoscompras


    