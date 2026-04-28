from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.db.models.functions import Cast
from datetime import date
from django.contrib import messages
from django.http import JsonResponse
from .models import TaInventario, TaProducto, TaMotivo

# Create your views here.
@login_required(login_url='inventory_auth:login')
def dashboard_view(request):
    total_productos = TaInventario.objects.filter(tipoInventario=1).count()
    productos_stock_bajo = TaInventario.objects.filter(tipoInventario=1).values('producto').annotate(
        total_registros=Count('id')
    ).filter(total_registros__lt=5).count()
    resultado = TaInventario.objects.aggregate(
    total_ingresos=Count('id', filter=Q(tipoInventario=1)),
    total_egresos=Count('id', filter=Q(tipoInventario=2)),
    )

    ingresos = resultado['total_ingresos']
    egresos = resultado['total_egresos']

    porcentaje = (egresos / ingresos * 100) if ingresos > 0 else 0
    return render(request, 'inventory/dashboard.html', {
        'total_productos': total_productos,
        'productos_stock_bajo': productos_stock_bajo,
        'porcentaje_total': porcentaje
    })

@login_required(login_url='inventory_auth:login')
def top_productos_view(request):
    top_productos = (
        TaInventario.objects
        .filter(tipoInventario=2)
        .values('producto__nombre')   # ← ajusta al nombre real del campo
        .annotate(total_ventas=Count('id'))
        .order_by('-total_ventas')[:5]
    )

    data = {
        'labels': [p['producto__nombre'] for p in top_productos],
        'ventas': [p['total_ventas'] for p in top_productos],
    }

    return JsonResponse(data)

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

            messages.success(request, f'Egresos registrados: {producto.nombre} x {cantidad}')
            return redirect('inventory:inventory-entry')
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
    productos = TaInventario.objects.filter(tipoInventario=1).values(
        'producto__id',
        'producto__nombre'
    ).distinct()
    motivos = TaMotivo.objects.values('id', 'descripcion')

    if request.method == 'POST':
        producto_id = request.POST.get("producto")
        motivo_id = request.POST.get("motivo")

        if not producto_id or not motivo_id:
            messages.error(request, 'Por favor complete todos los campos')
            return redirect('inventory:inventory-entry')
        
        try:
            producto = TaProducto.objects.get(id=producto_id)
            motivo = TaMotivo.objects.get(id=motivo_id)

            inventario = TaInventario(
                tipoInventario_id=2,
                producto=producto,
                usuario=request.user,
                motivo=motivo
            )

            inventario.save()

            inventario = TaInventario.objects.filter(tipoInventario=1, producto=producto).first()

            if inventario:
                inventario.delete()

            messages.success(request, f'Ingresos registrados: {producto.nombre}')
            return redirect('inventory:inventory-outs')
        except TaProducto.DoesNotExist:
            messages.error(request, 'El producto no existe')
            return redirect('inventory:inventory-entry')
    return render(request, 'inventory/inventory-outs.html', {
        'inventarios': inventarios,
        'total_inventarios': total_inventarios,
        'producto_top': producto_top,
        'inventarios_entrada': productos,
        'motivos': motivos
    })