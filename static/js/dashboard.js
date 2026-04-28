async function cargarTopProductos() {
    try {
        const response = await fetch('/inventory/top-productos');  // ← ajusta la URL
        const data = await response.json();

        const topProductsCtx = document.getElementById('topProductsChart').getContext('2d');

        new Chart(topProductsCtx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Ventas',
                    data: data.ventas,
                    backgroundColor: '#4f46e5',
                    borderRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

    } catch (error) {
        console.error('Error al cargar los productos:', error);
    }
}

// Gráfica de anillo - Distribución por categoría
const categoriesCtx = document.getElementById('categoriesChart').getContext('2d');
const categoriesChart = new Chart(categoriesCtx, {
    type: 'doughnut',
    data: {
        labels: ['Electrónica', 'Ropa', 'Alimentos', 'Hogar'],
        datasets: [{
            data: [30, 25, 25, 20],
            backgroundColor: ['#4f46e5', '#10b981', '#f59e0b', '#ef4444']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                display: false
            }
        }
    }
});

// Generar leyenda personalizada
const legendContainer = document.getElementById('categoriesLegend');
categoriesChart.data.labels.forEach((label, index) => {
    const legendItem = document.createElement('div');
    legendItem.className = 'legend-item';
    legendItem.innerHTML = `
        <span class="legend-color" style="background-color: ${categoriesChart.data.datasets[0].backgroundColor[index]}"></span>
        <span class="legend-label">${label}</span>
    `;
    legendContainer.appendChild(legendItem);
});

document.addEventListener('DOMContentLoaded', async () => {
    await cargarTopProductos();
});