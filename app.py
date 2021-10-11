from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/detallefunciones', methods=['GET'])
def detallefunciones():
    return render_template('detallefunciones.html')

@app.route('/busqueda', methods=['GET','POST'])
def busqueda():
    return render_template('busqueda.html')

@app.route('/informacion', methods=['GET'])
def informacion():
    return render_template('informacion.html')