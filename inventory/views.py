from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='inventory_auth:login')
def dashboard_view(request):
    return render(request, 'inventory/dashboard.html')

@login_required(login_url='inventory_auth:login')
def inventory_entry_view(request):
    return render(request, 'inventory/inventory-entry.html')

@login_required(login_url='inventory_auth:login')
def inventory_outs_view(request):
    return render(request, 'inventory/inventory-outs.html')