from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('inventory-entry/', views.inventory_entry_view, name='inventory-entry'),
]