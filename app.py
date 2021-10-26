from flask import Flask, render_template, request,redirect,session
import db
from sqlite3 import Error
import werkzeug.security as sec

app = Flask(__name__)
app.secret_key = "Secret Key"

peliculas=["Shang-chi", "Sin tiempo para morir","Venom","Spidey","Jhon Wick 4","Liga de la Justicia","Space Jam","Escape Room 2","Jack en la caja maldita","Cruella"]


@app.route('/', methods=['GET'])
def presentacion():
    return render_template('presentacion.html')

@app.route('/registro', methods=['GET','POST'])
def registro():
    return render_template('registro.html')

@app.route('/funciones', methods=['GET'])
def funciones():
    return render_template('funciones.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/agregarPelicula', methods=['GET','POST'])
def dashboardA():
    return render_template('dashboardA.html') 
   
@app.route('/Dfunciones', methods=['GET','POST'])
def dashboardF():
    return render_template('dashboardF.html') 

@app.route('/peliculas', methods=['GET','POST'])
def dashboardP():
    return render_template('dashboardP.html') 

@app.route('/usuario', methods=['GET','POST'])
def dashboardU():
    return render_template('dashboardU.html')     

@app.route('/detallefunciones/<idpelicula>', methods=['GET'])
def detallefunciones(idpelicula):
    if idpelicula == "shang-chi":
        return render_template('detallefunciones.html')
    if idpelicula == "sintiempoparamorir":
        return render_template('detallefuncion2.html')
    else:
        return render_template('detallefuncion3.html')
    

@app.route('/informacion', methods=['GET'])
def informacion():
    return render_template('informacion.html')

@app.route('/busqueda', methods=['GET'])
def busqueda():
    buscado = request.args.get('busqueda')
    if buscado in peliculas:
        if buscado=="Shang-chi":
            return render_template('detallefunciones.html')
        if buscado=="Sin tiempo para morir":
            return render_template('detallefuncion2.html')
        else:
            return render_template('detallefuncion3.html')
    else:
        resultado ="película no encontrada"
        return render_template('busqueda.html',buscado=buscado, resultado=resultado)

@app.route('/perfilusuario/<user>')
def perfilusuario(user):
    datos = db.consultardatos(session['user'])
    return render_template('perfilusuario.html', datos=datos)

@app.route('/validar-usuario', methods=['GET','POST'])
def validarusuario():
    usuario= request.form['usuario']
    contraseña= request.form['password']
    if validarUserPass(usuario,contraseña):
        if usuario=="administrador1":
            return render_template('dashboard.html')
            
        else:
            datos = db.consultardatos(session['user'])
            return render_template('perfilusuario.html', user=usuario, datos=datos)
            
    else:
        denegado= True
        return render_template('presentacion.html', denegado=denegado   )

def validarUserPass(usuario,contraseña):
    conexion=db.get_db()
    strsql="SELECT * FROM usuario WHERE usuario = '{}'".format(usuario)
    cursor=conexion.cursor()
    cursor.execute(strsql)
    datos=cursor.fetchall()
    cursor.close()
    if datos:
        if sec.check_password_hash(datos[0][4],contraseña):
            session.clear()
            session['user']=usuario
            return True
        else: return False
    else:
        return False

def registrar(id,nombre,usuario,correo,contraseña,fecha,tipodedocumento,celular,departamento,ciudad):
    try:
        conexion=db.get_db()
        strsql=("INSERT INTO usuario (id,nombre,usuario,correo,contraseña,fecha,tipoDeDocumento,celular,departamento,ciudad)" + " VALUES ("+"{},"+"'{}',"+"'{}',"+"'{}',"+"'{}',"+"'{}',"+"'{}',"+"{},"+"'{}',"+"'{}'"+");").format(id,nombre,usuario,correo,contraseña,fecha,tipodedocumento,celular,departamento,ciudad)
        cursor=conexion.cursor()
        cursor.execute(strsql)
        conexion.commit()
        conexion.close()
        cursor.close
        return True
    except Error:
        return False

@app.route('/validacion-registro',methods=['GET','POST'])
def validacion_registro():
    id = request.form['doc']
    nom = request.form['nombres']
    apellidos = request.form['apellidos']
    nombre=nom+" "+apellidos
    usuario = request.form['usuario']
    correo = request.form['email']
    contraseña = sec.generate_password_hash(request.form['contraseña'])
    fecha = request.form['fecha']
    tipodedocumento = request.form['selector']
    celular= request.form['celular']
    departamento = request.form['departamento']
    ciudad= request.form['ciudad']
    if(registrar(id,nombre,usuario,correo,contraseña,fecha,tipodedocumento,celular,departamento,ciudad)):
        registrado= "Usuario registrado con éxito"
    else:
        registrado= "No se ha registrado el usuario, el usuario o sus credenciales ya existen"
    return render_template('presentacion.html', registrado=registrado)

@app.route('/cerrarsesion')
def cerrar_sesion():
    if 'user' in session:
        session.pop('user')
        return redirect('/')

@app.route('/updatedatos', methods=['GET','POST'])
def actualizardatos():

    id = request.form['documento']
    nombre = request.form['nombre']
    usuario = session['user']
    correo = request.form['correo']
    contraseña = sec.generate_password_hash(request.form['contraseña'])
    fecha = request.form['fnacimiento']
    tipoDeDocumento = request.form['tcedula']
    celular= request.form['celular']
    departamento = request.form['departamento']
    ciudad= request.form['ciudad']

    datos = db.consultardatos(session['user'])
    db.actualizarusuario(id,nombre,usuario,correo,contraseña,fecha,tipoDeDocumento,celular,departamento,ciudad)
    return render_template('perfilusuario.html', user=usuario, datos=datos)

@app.route('/editarpu')
def editarpu():
    datos = db.consultardatos(session['user'])
    return render_template('editarpu.html', datos=datos)
