from django.db import models

# Create your models here.

class categoriaProducto(models.Model):
    nom_cat = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoría de producto"
        verbose_name_plural = "categorías de productos"
    
    def __str__(self):
        return self.nom_cat

class Producto(models.Model):
    nom_prod = models.CharField(max_length=60)
    categorias = models.ForeignKey(categoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="picstienda", null=True, blank=True)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
