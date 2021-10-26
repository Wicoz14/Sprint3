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


