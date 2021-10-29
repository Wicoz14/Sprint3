from flask import Flask, render_template, request,redirect,session, send_from_directory
import db
import os
from sqlite3 import Error
import werkzeug.security as sec

app = Flask(__name__)
app.secret_key = "Secret Key"

@app.before_request
def antes_peticion():
    if 'user' not in session and request.endpoint in ['perfilusuario','dashboard','presentacionA','presentacionP','presentacionF','dashboardU']:
       return redirect('/')
    elif 'user' in session and request.endpoint in ['registro']:
        return redirect('/perfilusuario/{}'.format(session['user']))
    elif 'user' in session and session['user']!= "admi1" and  request.endpoint in ['registro','dashboard','presentacionA','presentacionP','presentacionF','dashboardU']:   
        return redirect('/')



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
        datosEdit=[("","","","","","","","",""," "," ")]
        return render_template("dashboardA.html", action=action, datosEdit=datosEdit)
    else:
        nombre = request.form['nombre'] 
        duracion=request.form['duracion'] 
        director=request.form['director'] 
        genero=request.form['genero'] 
        trailer=request.form['link']
        estreno=request.form['fecha_estreno']
        actores=request.form['actores']
        sinopsis=request.form['sinopsis'] 
        caratula= request.files['files']
        pancarta=request.files['files_pancarta']

       

        caratula_final = "/static/assets/images/carteleras/C-{}".format(caratula.filename)
        pancarta_final = "/static/assets/images/carteleras/P-{}".format(pancarta.filename)

        db.agregar_pelicula(nombre,duracion,director,genero,trailer,estreno,actores,sinopsis,caratula_final,pancarta_final)
  

        caratula.save(os.getcwd() + "/static/assets/images/carteleras/" + 'C-' + caratula.filename )
        pancarta.save(os.getcwd() + "/static/assets/images/carteleras/" + 'P-'+ pancarta.filename )

       
        return redirect('/agregarPelicula')

@app.route('/peliculas', methods=['GET','POST'])
def presentacionP():
    if(request.method=='GET'):
        mostrar = db.mostrar_tabla("peliculas")
        return  render_template("dashboardP.html", tablapeli = mostrar)
    else:
        peli = request.form['nombrePelicula']
        mostrar = db.consultar_dato("peliculas","nombre='{}'".format(peli)," ")
        return render_template('dashboardP.html', tablapeli = mostrar) 

@app.route('/peliculas/<id>/<condicion>', methods=['GET','POST'])
def peliculasEE(id, condicion):
    if condicion == "Delete":   
        datoEliminar = db.consultar_dato('peliculas', 'peli_id={}'.format(id)," ")
        os.remove(os.getcwd() + datoEliminar[0][9])
        os.remove(os.getcwd() + datoEliminar[0][10]) 
        
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
            actores=request.form['actores']
            sinopsis=request.form['sinopsis'] 
            caratula = request.files['files']
            pancarta = request.files['files_pancarta']
            """ print(caratula) """
            
            peliculaEditar = db.consultar_dato('peliculas', 'peli_id={}'.format(id)," ")
            if caratula:
                os.remove(os.getcwd() + peliculaEditar[0][9])
                caratula.save(os.getcwd() + "/static/assets/images/carteleras/" +'C-' + caratula.filename )
                caratula_actualizada = "/static/assets/images/carteleras/" + "C-" + caratula.filename 
            else: 
                caratula_actualizada = peliculaEditar[0][9]
            
            if pancarta:
                os.remove(os.getcwd() + peliculaEditar[0][10])
                pancarta.save(os.getcwd() + "/static/assets/images/carteleras/" + 'P-' + pancarta.filename )
                pancarta_actualizada = "/static/assets/images/carteleras/" + 'P-' + pancarta.filename  
            else:
                pancarta_actualizada = peliculaEditar[0][10]


           
                


           
            
            db.editar_pelicula("nombre='{}'".format(nombre),"duracion='{}'".format(duracion),"director='{}'".format(director),"genero='{}'".format(genero), "trailer='{}'".format(trailer), "fechaEstreno='{}'".format(estreno), "actores='{}'".format(actores), "sinopsis='{}'".format(sinopsis),"caratula='{}'".format(caratula_actualizada),"pancarta='{}'".format(pancarta_actualizada), "peli_id={}".format(id))

            return redirect("/peliculas")

@app.route('/Dfuncion', methods=['GET','POST'])
def presentacionF():     
    if(request.method == 'GET'): 
        mostrar = db.mostrar_tabla("funciones")
        datosEdit=[("","","","","","","")]
        action = "/Dfuncion"
        return render_template("dashboardF.html", tablafunc = mostrar, datosEdit = datosEdit, action=action)       
    else:
        peliculaadmi1 = request.form['pelicula']
        id = request.form['id']
        formato=request.form['formato']
        fecha = request.form['fecha']
        hora = request.form['hora']
        sala = request.form['sala']
        capacidad = request.form['capacidad']
        

        consulta = db.consultar_dato("peliculas","peli_id='{}'".format(id), " ")

       

        if consulta and (str(consulta[0][1]).replace(" ","") == peliculaadmi1.replace(" ","")):
            ''' consulta = db.consultar_dato("peliculas","nombre='{}'".format(pelicula), " ")
            print(len(consulta))
            id=consulta[0][0] '''
            
            db.agregar_funcion(peliculaadmi1,id,formato,fecha,hora,sala,capacidad)
            return redirect('/Dfuncion')
        elif consulta and (str(consulta[0][1]).replace(" ","") != peliculaadmi1.replace(" ","")):
            mostrar = db.mostrar_tabla("funciones")
            msj="Id o pelicula equivocados"
            datosEdit=[(" "," "," "," "," "," "," ")]
            action = "/Dfuncion"
            return render_template("dashboardF.html", tablafunc = mostrar, msj=msj,datosEdit = datosEdit, action=action)
        elif not consulta:
            mostrar = db.mostrar_tabla("funciones")
            msj="La pelicula no existe"
            datosEdit=[(" "," "," "," "," "," "," ")]
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
        formato=request.form['formato']
        fecha = request.form['fecha']
        hora = request.form['hora']
        sala = request.form['sala']
        capacidad = request.form['capacidad']
        
        db.editar_funcion("pelicula='{}'".format(pelicula),"peli_id={}".format(id_peli),"formato='{}'".format(formato), "fecha='{}'".format(fecha),"hora='{}'".format(hora),"sala='{}'".format(sala), "capacidad={}".format(capacidad),"id={}".format(id))   
       
        return redirect('/Dfuncion')
    

@app.route('/Dfunciones/eliminar/<id>')
def funcionesEE(id):
    db.elminar_dato("funciones","id='{}'".format(id))
    return redirect('/Dfuncion')
    


@app.route('/usuario', methods=['GET','POST'])
def dashboardU():
    if(request.method == 'GET'): 
        mostrar = db.mostrar_tabla("usuario")
        return render_template("dashboardU.html", tablaUsuario = mostrar )       
    else:
        id = request.form['id']
        mostrar = db.consultar_dato("usuario","id={}".format(id)," ")
        return render_template('dashboardU.html', tablaUsuario = mostrar)    

@app.route('/usuario/eliminar/<id>')
def eliminarUsuario(id):
    db.elminar_dato("usuario","id={}".format(id))
    return redirect('/usuario')

@app.route('/detallefunciones/<idpelicula>', methods=['GET'])
def detallefunciones(idpelicula):
    funcion= db.retornar_detalle_funcion(idpelicula)
    return render_template('detallefunciones.html', funcion=funcion)

@app.route('/informacion', methods=['GET'])
def informacion():
    return render_template('informacion.html')

@app.route('/busqueda/<peliculadmi1a>', methods=['GET'])
def busqueda(pelicula):
    busqueda= db.retornar_busqueda(pelicula)
    return render_template('busqueda.html',busqueda=busqueda, pelicula=pelicula)
    
@app.route('/perfilusuario/<user>')
def perfilusuario(user):
    datos = db.consultardatos(session['user'])
    return render_template('perfilusuario.html', datos=datos)

@app.route('/validar-usuario', methods=['GET','POST'])
def validarusuario():
    usuario= request.form['usuario']
    contraseña= request.form['password']
    if validarUserPass(usuario,contraseña):
        if usuario=="admi1":
            return redirect('/dashboard')
            
        else:
            datos = db.consultardatos(session['user'])
            return render_template('perfilusuario.html', user=usuario, datos=datos)
            
    else:
        denegado= True
        estrenos= db.retornar_estrenos()
        return render_template('presentacion.html',denegado=denegado,estrenos=estrenos )

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
    estrenos= db.retornar_estrenos()
    return render_template('presentacion.html', registrado=registrado, estrenos=estrenos)

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

@app.route('/infocompras', methods=['GET','POST'])
def infcompras():
    datoscompras = db.consultar_compras(session['user'])
    print(datoscompras)
    if datoscompras == []:
        return render_template("compras.html", nocompras="No has realizado ninguna compra, podras realizarlas en la seccion de funciones")
    else:
        return render_template('compras.html', datoscompras=datoscompras)
