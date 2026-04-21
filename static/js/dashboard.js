// Gráfica de barras - Productos más vendidos
const topProductsCtx = document.getElementById('topProductsChart').getContext('2d');
new Chart(topProductsCtx, {
    type: 'bar',
    data: {
        labels: ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
        datasets: [{
            label: 'Ventas',
            data: [120, 95, 150, 110, 130],
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