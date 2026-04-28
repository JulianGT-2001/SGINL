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
    const outsModal = document.getElementById('outsModal');
    const btnNewEntry = document.querySelector('.btn-new-entry');
    const closeOutsModalBtn = document.getElementById('closeOutsModalBtn');
    const cancelOutsBtn = document.getElementById('cancelOutsBtn');
    const saveOutsBtn = document.getElementById('saveOutsBtn');
    const outsForm = document.getElementById('outsForm');

    // Abrir modal
    btnNewEntry.addEventListener('click', function() {
        outsModal.classList.add('show');
    });

    // Cerrar modal
    closeOutsModalBtn.addEventListener('click', function() {
        outsModal.classList.remove('show');
        outsForm.reset();
    });

    cancelOutsBtn.addEventListener('click', function() {
        outsModal.classList.remove('show');
        outsForm.reset();
    });

    // Cerrar al hacer click fuera
    window.addEventListener('click', function(event) {
        if (event.target === outsModal) {
            outsModal.classList.remove('show');
            outsForm.reset();
        }
    });

    // Guardar datos
    saveOutsBtn.addEventListener('click', async function() {
        if (outsForm.checkValidity()) {
            var producto = document.getElementById('productSelectOuts').value;
            var motivo = document.getElementById('motivoSelectOuts').value;

            var response = await fetch(window.location.pathname, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new URLSearchParams({
                    producto: producto,
                    motivo: motivo
                })
            });

            if (response.ok)
            {
                outsModal.classList.remove('show');
                outsForm.reset();
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
