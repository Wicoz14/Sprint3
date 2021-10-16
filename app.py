from flask import Flask, render_template, request,redirect

app = Flask(__name__)

peliculas=["shang-chi", "sin tiempo para morir"]
usuarios={"usuario1":'12345', "usuario2":'67890',"admi1":'admi12345'}

@app.route('/', methods=['GET','POST'])
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

@app.route('/detallefunciones/<idpelicula>', methods=['GET'])
def detallefunciones(idpelicula):
    return render_template('detallefunciones.html')

@app.route('/informacion', methods=['GET'])
def informacion():
    return render_template('informacion.html')

@app.route('/busqueda', methods=['GET'])
def busqueda():
    buscado = request.args.get('busqueda')
    if buscado in peliculas:
        resultado ="encontrada"
    else:
        resultado ="película no encontrada"
    return render_template('busqueda.html',buscado=buscado, resultado=resultado)

@app.route('/perfilusuario', methods=['POST'])
def perfilusuario():
    usuario= request.form['usuario']
    if usuario=="admi1":
        return render_template('dashboard.html')
    else:
        return render_template('perfilusuario.html', user=usuario)
    