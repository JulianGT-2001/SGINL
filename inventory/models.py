from django.db import models
from django.conf import settings

# Create your models here.
class TaCategoria(models.Model):
    descripcion = models.CharField(max_length=200)
    fechaRegistro = models.DateTimeField(auto_now_add=True, db_column='fecha_registro')
    fechaActualizacion = models.DateTimeField(auto_now_add=True, db_column='fecha_actualizacion')
    class Meta:
        ordering = ['descripcion']
        indexes = [
            models.Index(fields=['descripcion'])
        ]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'ta_categoria'

    def __str__(self):
        return self.descripcion
    
class TaProducto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaRegistro = models.DateTimeField(auto_now_add=True, db_column='fecha_registro')
    fechaActualizacion = models.DateTimeField(auto_now_add=True, db_column='fecha_actualizacion')

    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['nombre']),
            models.Index(fields=['-fechaRegistro']),
        ]
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        db_table = 'ta_producto'
    
    def __str__(self):
        return self.nombre
    
class TaProductoCategoria(models.Model):
    producto = models.ForeignKey(TaProducto, on_delete=models.CASCADE, db_column='producto_id')
    categoria = models.ForeignKey(TaCategoria, on_delete=models.CASCADE, db_column='categoria_id')
    fechaRegistro = models.DateTimeField(auto_now_add=True, db_column='fecha_registro')
    fechaActualizacion = models.DateTimeField(auto_now_add=True, db_column='fecha_actualizacion')

    class Meta:
        db_table = 'ta_producto_categoria'
        unique_together = (('producto', 'categoria'),)

    def __str__(self):
        return f"{self.producto.nombre} - {self.categoria.descripcion}"
    
class TaMotivo(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now_add=True, db_column='fecha_registro')

    class Meta:
        verbose_name = 'motivo'
        verbose_name_plural = 'motivos'
        db_table = 'ta_motivo'

    def __str__(self):
        return self.descripcion
    
class TaTipoInventario(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now_add=True, db_column='fecha_registro')

    class Meta:
        verbose_name = 'tipo de inventario'
        verbose_name_plural = 'tipos de inventarios'
        db_table = 'ta_tipo_inventario'

    def __str__(self):
        return self.descripcion
    
class TaInventario(models.Model):
    tipoInventario = models.ForeignKey(TaTipoInventario, on_delete=models.CASCADE, db_column='tipo_inventario_id')
    producto = models.ForeignKey(TaProducto, on_delete=models.CASCADE, db_column='producto_id')
    motivo = models.ForeignKey(TaMotivo, on_delete=models.CASCADE, db_column='motivo_id', null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='usuario_id')
    fechaRegistro = models.DateTimeField(auto_now_add=True, db_column='fecha_registro')

    class Meta:
        verbose_name = 'inventario'
        verbose_name_plural = 'inventarios'
        db_table = 'ta_inventario'

    def __str__(self):
        return f"{self.producto.nombre} - {self.tipoInventario.descripcion} - {self.usuario}"