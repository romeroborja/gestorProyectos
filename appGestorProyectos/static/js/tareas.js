function cargarDatos(filtro) {
    let url = "http://127.0.0.1:8000/tareasAPI/"
    fetch(url)
        .then((respuesta) => respuesta.json())
        .then((datos) => {
            crearTablaTareas(datos, filtro)
        })
}

cargarDatos("");

document.getElementById('select').addEventListener('change', function(event) {
    cargarDatos(event.target.value);
});

function crearCabecera(){
    let cabecera = `
        <tr>
            <th>Nombre</th>
            <th>Fecha de inicio</th>
            <th>Fecha de entrega</th>
            <th>Estado de la tarea</th>
            <th>Más acciones</th>
        </tr>
    `
    return cabecera;
}

function crearFila(objeto){
    console.log(objeto.nombre)
    let fila = `
        <tr>
            <td>${objeto.nombre}</td>
            <td>${objeto.fecha_inicio}</td>
            <td>${objeto.fecha_fin}</td>
            <td>${objeto.estado_tarea}</td>
            <td style="text-align: center;"><a class="btn btn-warning" href="/tarea/${objeto.id}">Mostrar más</a></td>
        </tr>
    `
    return fila;
}

function crearTabla(array, filtro) {
    let cabecera = '<thead>' + crearCabecera() + '</thead>';
    let tabla = cabecera + '<tbody>';
    for (const objeto of array) {
        if(objeto.estado_tarea == filtro) {
            tabla += crearFila(objeto);
        }else if(filtro === "") {
            tabla += crearFila(objeto);
        }
    }
    tabla += '</tbody>';
    return tabla;
}

function crearTablaTareas(tareas, filtro) {
    let tablaINSERT = crearTabla(tareas, filtro);
    document.getElementById('tabla').innerHTML = tablaINSERT;
}

