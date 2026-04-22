from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date
from .models import TaInventario, TaProducto

# Create your views here.
@login_required(login_url='inventory_auth:login')
def dashboard_view(request):
    return render(request, 'inventory/dashboard.html')

@login_required(login_url='inventory_auth:login')
def inventory_entry_view(request):
    inventarios = TaInventario.objects.all().filter(tipoInventario=1)
    total_inventarios = TaInventario.objects.filter(
        tipoInventario=1,
        fechaRegistro__date=date.today()
    ).count()
    producto_top_stat = TaInventario.objects.filter(tipoInventario=1).values('producto').annotate(
        cantidad=Count('producto')
    ).order_by('-cantidad').first()
    if producto_top_stat:
        producto_top = TaProducto.objects.get(id=producto_top_stat['producto'])
    else:
        producto_top = None
    return render(request, 'inventory/inventory-entry.html', {
        'inventarios': inventarios,
        'total_inventarios': total_inventarios,
        'producto_top': producto_top
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