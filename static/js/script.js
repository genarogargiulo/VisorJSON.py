var socket = io();

socket.on('nuevo_mensaje', function(data) {
    var nuevoMensaje = crearMensajeElemento(data);
    insertarMensajeEnLista(nuevoMensaje);
});

function crearMensajeElemento(data) {
    var nuevoMensaje = document.createElement('li');
    var fechaHora = obtenerFechaHoraActual();
    var mensajeJSON = JSON.stringify(data.mensaje, null, 2); // Formatear el JSON con 2 espacios de indentación

    nuevoMensaje.innerHTML = `
        <strong>Fecha y hora:</strong> ${fechaHora}<br>
        <strong>URL:</strong> ${data.url}<br>
        <strong>Header:</strong><br>${formatoHeader(data.header)}<br>
        <strong>Mensaje:</strong><pre class='json-container'>${mensajeJSON}</pre>
    `;
    
    return nuevoMensaje;
}

function obtenerFechaHoraActual() {
    var opcionesFechaHora = {
        year: 'numeric', month: 'numeric', day: 'numeric',
        hour: '2-digit', minute: '2-digit', second: '2-digit'
    };
    return new Date().toLocaleString('es-ES', opcionesFechaHora);
}

function formatoHeader(header) {
    var formato = '';
    for (var key in header) {
        formato += `<span><strong>${key}:</strong> ${header[key]}</span><br>`;
    }
    return formato;
}

function insertarMensajeEnLista(mensajeElemento) {
    var listaMensajes = document.getElementById('mensajes-list');
    var primerElemento = listaMensajes.firstChild; // Obtener el primer elemento de la lista
    if (primerElemento) {
        listaMensajes.insertBefore(mensajeElemento, primerElemento); // Insertar el nuevo mensaje antes del primer elemento
    } else {
        listaMensajes.appendChild(mensajeElemento); // Si no hay ningún mensaje, simplemente añadirlo
    }
}

