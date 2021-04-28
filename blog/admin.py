from django.contrib import admin
from .models import Categoria, Entrada

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'updated')


class EntradaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'updated')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Entrada, EntradaAdmin)