from django.contrib import admin
from .models import categoriaProducto, Producto

# Register your models here.

class catProdAdm(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class prodAdm(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    

admin.site.register(categoriaProducto, catProdAdm)
admin.site.register(Producto, prodAdm)


