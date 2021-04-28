from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nomcat = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoría'           # CUANDO HAY 1 REG EN LA TABLA
        verbose_name_plural = 'categorías'   # CUANDO HAY >1 REG EN LA TABLA

    def __str__(self):
        return self.nomcat


class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='blog', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    # RELACIONES
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name = 'entrada'           # CUANDO HAY 1 REG EN LA TABLA
        verbose_name_plural = 'entradas'   # CUANDO HAY >1 REG EN LA TABLA

    def __str__(self):
        return self.titulo
