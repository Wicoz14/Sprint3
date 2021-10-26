from flask import Flask, render_template, request,redirect,session, send_from_directory
import db
import os
from sqlite3 import Error
import werkzeug.security as sec

app = Flask(__name__)
app.secret_key = "Secret Key"

@app.before_request
def antes_peticion():
    if 'user' not in session and request.endpoint in ['perfilusuario']:
       return redirect('/')
    elif 'usuario' in session and request.endpoint in ['registro']:
        return redirect('/perfilusuario/{}'.format(session['user']))

@app.route('/', methods=['GET'])
def presentacion():
    estrenos= db.retornar_estrenos()
    return render_template('presentacion.html',estrenos=estrenos)

@app.route('/registro', methods=['GET','POST'])
def registro():
    return render_template('registro.html')

@app.route('/funciones', methods=['GET'])
def funciones():
    funciones =db.retornar_funciones()
    return render_template('funciones.html',funciones=funciones)

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/agregarPelicula', methods=['GET','POST'])
def presentacionA(): 
    if(request.method == 'GET'): 
        action="/agregarPelicula"
        datosEdit=[(" "," "," "," "," "," "," "," ")]
        return render_template("dashboardA.html", action=action, datosEdit=datosEdit)
    else:
        nombre = request.form['nombre'] 
        duracion=request.form['duracion'] 
        director=request.form['director'] 
        genero=request.form['genero'] 
        trailer=request.form['link']
        estreno=request.form['fecha_estreno']
        sinopsis=request.form['sinopsis'] 
        caratula= request.files['files']
        caratula.save(os.getcwd() + "/static/assets/images/carteleras/" + caratula.filename )
        caratula_final = "/static/assets/images/carteleras/{}".format(caratula.filename)
        db.agregar_pelicula(nombre,duracion,director,genero,trailer,estreno,sinopsis,caratula_final)

        return redirect('/agregarPelicula')

@app.route('/peliculas', methods=['GET','POST'])
def presentacionP():
    mostrar = db.mostrar_tabla("peliculas")
    return  render_template("dashboardP.html", tablapeli = mostrar)

@app.route('/peliculas/<id>/<condicion>', methods=['GET','POST'])
def peliculasEE(id, condicion):
    if condicion == "Delete":   
        caratulaEliminar = db.consultar_dato('peliculas', 'peli_id={}'.format(id)," ")
        os.remove(os.getcwd() + caratulaEliminar[0][8])
        
        db.elminar_dato("peliculas","peli_id={}".format(id))
        return redirect('/peliculas')  

    if condicion == "Update":
        if(request.method == 'GET'):    
            datosEdit = db.consultar_dato("peliculas", "peli_id='{}'".format(id), " ") 
            action="/peliculas/{}/{}".format(id,condicion)
            
            return render_template("dashboardA.html",  datosEdit = datosEdit, action=action )
        else:
            nombre = request.form['nombre'] 
            duracion=request.form['duracion'] 
            director=request.form['director'] 
            genero=request.form['genero'] 
            trailer=request.form['link']
            estreno=request.form['fecha_estreno']
            sinopsis=request.form['sinopsis'] 
            caratula = request.files['files']

            consulta = db.consultar_dato("peliculas", "caratula= '/static/assets/images/carteleras/{}'".format(caratula.filename), " ") 
            print(consulta)
            if not consulta:
                caratulaEliminar = db.consultar_dato('peliculas', 'peli_id={}'.format(id)," ")

                os.remove(os.getcwd() + caratulaEliminar[0][8])
                caratula.save(os.getcwd() + "/static/assets/images/carteleras/" + caratula.filename )
                caratula_actualizada = "/static/assets/images/carteleras/" + caratula.filename
            else:
                caratula_actualizada = "/static/assets/images/carteleras/" + caratula.filename

           
            
            db.editar_pelicula("nombre='{}'".format(nombre),"duracion='{}'".format(duracion),"director='{}'".format(director),"genero='{}'".format(genero), "trailer='{}'".format(trailer), "fechaEstreno='{}'".format(estreno), "sinopsis='{}'".format(sinopsis),"caratula='{}'".format(caratula_actualizada),"peli_id={}".format(id))

            return redirect("/peliculas")

@app.route('/Dfuncion', methods=['GET','POST'])
def presentacionF():     
    if(request.method == 'GET'): 
        mostrar = db.mostrar_tabla("funciones")
        datosEdit=[(" "," "," "," "," "," ")]
        action = "/Dfuncion"
        return render_template("dashboardF.html", tablafunc = mostrar, datosEdit = datosEdit, action=action)       
    else:
        pelicula = request.form['pelicula']
        id = request.form['id']
        fecha = request.form['fecha']
        hora = request.form['hora']
        sala = request.form['sala']
        capacidad = request.form['capacidad']
        

        cantidad = db.contar_dato("peliculas","peli_id='{}'".format(id))

        if cantidad[0][0] == 1:
            ''' consulta = db.consultar_dato("peliculas","nombre='{}'".format(pelicula), " ")
            print(len(consulta))
            id=consulta[0][0] '''
            
            db.agregar_funcion(pelicula,id,fecha,hora,sala,capacidad)
            return redirect('/Dfuncion')
        else:
            mostrar = db.mostrar_tabla("funciones")
            msj="La pelicula no existe"
            datosEdit=[(" "," "," "," "," "," ")]
            action = "/Dfuncion"
            return render_template("dashboardF.html", tablafunc = mostrar, msj=msj,datosEdit = datosEdit, action=action)

@app.route('/Dfunciones/<id>', methods=['GET','POST']) 
def función_editar(id):
    if(request.method == 'GET'): 
        mostrar = db.mostrar_tabla("funciones")    
        datosEdit = db.consultar_dato("funciones", "id='{}'".format(id), " ") 
        action="/Dfunciones/'{}'".format(id)
        
        return render_template("dashboardF.html", tablafunc = mostrar, datosEdit = datosEdit, action=action )
    else:    
        pelicula = request.form['pelicula']
        id_peli = request.form['id'] 
        fecha = request.form['fecha']
        hora = request.form['hora']
        sala = request.form['sala']
        capacidad = request.form['capacidad']
        
        db.editar_dato("funciones","pelicula='{}'".format(pelicula),"peli_id={}".format(id_peli), "fecha='{}'".format(fecha), "hora='{}'".format(hora), "sala='{}'".format(sala), "capacidad={}".format(capacidad),"id={}".format(id))   
       
        return redirect('/Dfuncion')
    

@app.route('/Dfunciones/<funcion>/<condicion>/<id>')
def funcionesEE(funcion, condicion, id):
    if condicion == "D":
        db.elminar_dato("funciones","id='{}'".format(id))
        return redirect('/Dfuncion')
    elif condicion == "U":
        ''' db.consultar_dato("funciones", "id='{}'".format(id)) '''
        return redirect('/Dfunciones/{}'.format(id))


@app.route('/usuario', methods=['GET','POST'])
def dashboardU():
    if(request.method == 'GET'): 
        mostrar = db.mostrar_tabla("usuario")
        return render_template("dashboardU.html", tablaUsuario = mostrar )       
    else:
        return render_template('dashboardU.html')     

@app.route('/detallefunciones/<idpelicula>', methods=['GET'])
def detallefunciones(idpelicula):
    funcion= db.retornar_detalle_funcion(idpelicula)
    return render_template('detallefunciones.html', funcion=funcion)

@app.route('/informacion', methods=['GET'])
def informacion():
    return render_template('informacion.html')

@app.route('/busqueda', methods=['GET'])
def busqueda():
    return render_template('busqueda.html')

@app.route('/perfilusuario/<user>')
def perfilusuario(user):
    return render_template('perfilusuario.html')

@app.route('/validar-usuario', methods=['GET','POST'])
def validarusuario():
    usuario= request.form['usuario']
    contraseña= request.form['password']
    if validarUserPass(usuario,contraseña):
        if usuario=="admi1":
            return render_template('dashboard.html')
            
        else:
            return render_template('perfilusuario.html', user=usuario)
            
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
