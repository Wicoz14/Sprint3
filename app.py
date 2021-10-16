from flask import Flask, render_template, request,redirect

app = Flask(__name__)

peliculas=["Shang-chi", "Sin tiempo para morir","Venom","Spidey","Jhon Wick 4","Liga de la Justicia","Space Jam","Escape Room 2","Jack en la caja maldita","Cruella"]
usuarios={"usuario1":'12345', "usuario2":'67890',"admi1":'admi12345'}

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
    if idpelicula == "Shang-chi":
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
        if buscado=="shang-chi":
            return render_template('detallefunciones.html')
        if buscado=="Sin tiempo para morir":
            return render_template('detallefuncion2.html')
        else:
            return render_template('detallefuncion3.html')
    else:
        resultado ="película no encontrada"
        return render_template('busqueda.html',buscado=buscado, resultado=resultado)

@app.route('/perfilusuario', methods=['GET','POST'])
def perfilusuario():
    usuario= request.form['usuario']
    if usuario=="admi1":
        return render_template('dashboard.html')
    else:
        return render_template('perfilusuario.html', user=usuario)
    