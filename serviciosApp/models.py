from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=20)
    describe = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='imagenes')
    creado = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servixio'           # CUANDO HAY 1 REG EN LA TABLA
        verbose_name_plural = 'servixios'   # CUANDO HAY >1 REG EN LA TABLA
    
    def __str__(self):
        return self.titulo
