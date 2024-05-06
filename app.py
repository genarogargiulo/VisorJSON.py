from flask import Flask, request, render_template
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv

app = Flask(__name__)




load_dotenv()  # Load environment variables from .env file if available


IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
icon = os.path.join(app.config['UPLOAD_FOLDER'], 'icon.png')
#print = os.path.join(app.config['UPLOAD_FOLDER'], 'print.png')
#reload = os.path.join(app.config['UPLOAD_FOLDER'], 'reload.png')

socketio = SocketIO(app)



# Datos temporales para almacenar los mensajes recibidos
mensajes = {
    "confirmacionEntrada": [],
    "confirmacionSalida": [],
    "ajusteStock": [],
    "stockActual": [],
    "actualizacionEstadosPedidos": [],
    "actualizacionCantidad": [],
    "resultadosOrdenEntrada": [],
    "resultadosPedidos": []
}

@app.route('/confirmacionEntrada', methods=['POST'])
def confirmacion_entrada():
    mensaje = request.json
    mensajes["confirmacionEntrada"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})

    return "Mensaje recibido correctamente"

@app.route('/confirmacionSalida', methods=['POST'])
def confirmacion_salida():
    mensaje = request.json
    mensajes["confirmacionSalida"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})
    return "Mensaje recibido correctamente"

@app.route('/ajusteStock', methods=['POST'])
def ajuste_stock():
    mensaje = request.json
    mensajes["ajusteStock"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})
    return "Mensaje recibido correctamente"

@app.route('/stockActual', methods=['POST'])
def stockActual():
    mensaje = request.json
    mensajes["stockActual"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})
    return "Mensaje recibido correctamente"

@app.route('/actualizacionEstadosPedidos', methods=['POST'])
def actualizacionEstadosPedidos():
    mensaje = request.json
    mensajes["actualizacionEstadosPedidos"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})
    return "Mensaje recibido correctamente"

@app.route('/actualizacionCantidad', methods=['POST'])
def actualizacionCantidad():
    mensaje = request.json
    mensajes["actualizacionCantidad"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})
    return "Mensaje recibido correctamente"

@app.route('/resultadosOrdenEntrada', methods=['POST'])
def resultadosOrdenEntrada():
    mensaje = request.json
    mensajes["resultadosOrdenEntrada"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})
    return "Mensaje recibido correctamente"

@app.route('/resultadosPedidos', methods=['POST'])
def resultadosPedidos():
    mensaje = request.json
    mensajes["resultadosPedidos"].append(mensaje)
    socketio.emit('nuevo_mensaje', {'url': request.url, 'header': dict(request.headers), 'mensaje': mensaje})
    return "Mensaje recibido correctamente"

@app.route('/')
def index():
    return render_template('index.html', mensajes=mensajes, img_icon=icon, img_logo=logo) #, img_print=print, img_reload=reload

if __name__ == '__main__':
    # Leer el puerto desde el archivo de configuración
    with open('config.properties', 'r') as f:
        port = int(f.read().split('=')[1])

    app.run(debug=True, port=port)