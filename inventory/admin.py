from django.contrib import admin
from .models import TaCategoria, TaProducto, TaProductoCategoria, TaMotivo, TaTipoInventario, TaInventario

# Register your models here.
@admin.register(TaCategoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'fechaRegistro']
    list_filter = ['descripcion', 'fechaRegistro']

@admin.register(TaProducto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'fechaRegistro']
    list_filter = ['nombre', 'fechaRegistro']
    list_editable = ['precio']

@admin.register(TaProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'categoria']

@admin.register(TaMotivo)
class MotivoAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'fechaRegistro']

@admin.register(TaTipoInventario)
class TipoInventarioAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'fechaRegistro']

@admin.register(TaInventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['tipoInventario', 'producto', 'motivo', 'usuario', 'fechaRegistro']
    list_filter = ['tipoInventario', 'producto', 'motivo', 'usuario', 'fechaRegistro']