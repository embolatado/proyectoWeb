from django.contrib import admin
from .models import Servicio

# Register your models here.
class extraServicio(admin.ModelAdmin):
    readonly_fields = ('creado', 'updated')

admin.site.register(Servicio, extraServicio)

