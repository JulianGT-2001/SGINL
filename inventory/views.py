from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date
from django.contrib import messages
from .models import TaInventario, TaProducto

# Create your views here.
@login_required(login_url='inventory_auth:login')
def dashboard_view(request):
    return render(request, 'inventory/dashboard.html')

@login_required(login_url='inventory_auth:login')
def inventory_entry_view(request):
    inventarios = TaInventario.objects.filter(tipoInventario=1).values(
        'producto__id',
        'producto__nombre'
    ).annotate(
        total_registros=Count('id')
    ).order_by('-total_registros')
    total_inventarios = TaInventario.objects.filter(
        tipoInventario=1,
        fechaRegistro__date=date.today()
    ).count()
    producto_top_stat = TaInventario.objects.filter(tipoInventario=1).values('producto').annotate(
        cantidad=Count('producto')
    ).order_by('-cantidad').first()
    productos = TaProducto.objects.values('id','nombre')
    if producto_top_stat:
        producto_top = TaProducto.objects.get(id=producto_top_stat['producto'])
    else:
        producto_top = None

    if request.method == 'POST':
        producto_id = request.POST.get("producto")
        cantidad = request.POST.get("cantidad")

        print(f'el producto es: {producto_id}')
        print(f'la cantidad es: {cantidad}')

        if not producto_id or not cantidad:
            messages.error(request, 'Por favor complete todos los campos')
            return redirect('inventory:inventory-entry')
        
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                messages.error(request, 'La cantidad debe ser mayor a 0')
                return redirect('inventory:inventory-entry')
            
            for i in range(cantidad):
                producto = TaProducto.objects.get(id=producto_id)

                inventario = TaInventario(
                    tipoInventario_id=1,
                    producto=producto,
                    usuario=request.user,
                    motivo_id=None
                )

                inventario.save()

            messages.success(request, f'Ingresos registrados: {producto.nombre} x {cantidad}')
        except TaProducto.DoesNotExist:
            messages.error(request, 'El producto no existe')
            return redirect('inventory:inventory-entry')
        except ValueError:
            messages.error(request, 'La cantidad debe de ser un número válido')
            return redirect('inventory:inventory-entry')
    return render(request, 'inventory/inventory-entry.html', {
        'inventarios': inventarios,
        'total_inventarios': total_inventarios,
        'producto_top': producto_top,
        'productos': productos
    })

@login_required(login_url='inventory_auth:login')
def inventory_outs_view(request):
    inventarios = TaInventario.objects.all().filter(tipoInventario=2)
    total_inventarios = TaInventario.objects.filter(
        tipoInventario=2,
        fechaRegistro__date=date.today()
    ).count()
    producto_top_stat = TaInventario.objects.filter(tipoInventario=2).values('producto').annotate(
        cantidad=Count('producto')
    ).order_by('-cantidad').first()
    if producto_top_stat:
        producto_top = TaProducto.objects.get(id=producto_top_stat['producto'])
    else:
        producto_top = None
    return render(request, 'inventory/inventory-outs.html', {
        'inventarios': inventarios,
        'total_inventarios': total_inventarios,
        'producto_top': producto_top
    })