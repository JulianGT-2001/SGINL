$(document).ready(function() {
    $('#productosTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excel',
                text: 'Descargar Excel',
                className: 'dt-button'
            },
            {
                extend: 'csv',
                text: 'Descargar CSV',
                className: 'dt-button'
            },
            {
                extend: 'print',
                text: 'Imprimir',
                className: 'dt-button'
            }
        ],
        language: {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        pageLength: 10,
        responsive: true
    });

    // Modal functionality
    const entryModal = document.getElementById('entryModal');
    const btnNewEntry = document.querySelector('.btn-new-entry');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    const saveBtn = document.getElementById('saveBtn');
    const entryForm = document.getElementById('entryForm');

    // Abrir modal
    btnNewEntry.addEventListener('click', function() {
        entryModal.classList.add('show');
    });

    // Cerrar modal con botón X
    closeModalBtn.addEventListener('click', function() {
        entryModal.classList.remove('show');
        entryForm.reset();
    });

    // Cerrar modal con botón Cancelar
    cancelBtn.addEventListener('click', function() {
        entryModal.classList.remove('show');
        entryForm.reset();
    });

    // Cerrar modal al hacer click fuera del contenido
    window.addEventListener('click', function(event) {
        if (event.target === entryModal) {
            entryModal.classList.remove('show');
            entryForm.reset();
        }
    });

    // Guardar formulario
    saveBtn.addEventListener('click', async function() {
        if (entryForm.checkValidity()) {
            // Aquí irá la lógica para guardar los datos
            var producto = document.getElementById('productSelect').value;
            var cantidad = document.getElementById('quantityInput').value;

            var response = await fetch(window.location.pathname, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new URLSearchParams({
                    producto: producto,
                    cantidad: cantidad
                })
            });

            if (response.ok)
            {
                entryModal.classList.remove('show');
                entryForm.reset();
                setTimeout(() => {
                    location.reload();
                }, 500);
                return;
            }

            alert("Ha ocurrido un error al guardar los ingresos")
            
        } else {
            alert('Por favor completa todos los campos');
        }
    });
});
