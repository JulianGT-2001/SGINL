// Sweet Alert Toast Configuration
const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 5000,
    timerProgressBar: true,
    didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
});

// Función para mostrar mensajes desde Django
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    const messageContainer = document.querySelector(".messages-container");

    alerts.forEach(alert => {
        const message = alert.textContent.trim();
        const className = alert.className;
        
        let icon = 'info';
        let background = '#0d6efd';
        
        if (className.includes('alert-success')) {
            icon = 'success';
            background = '#198754';
        } else if (className.includes('alert-error')) {
            icon = 'error';
            background = '#dc3545';
        } else if (className.includes('alert-warning')) {
            icon = 'warning';
            background = '#ffc107';
        }
        
        Toast.fire({
            icon: icon,
            title: message,
            background: background,
            color: '#fff'
        });
    });
    
    // Ocultar el contenedor de mensajes completamente
    if (messageContainer) {
        messageContainer.style.display = 'none';
    }
});
