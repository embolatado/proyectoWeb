from django.shortcuts import render
from .models import Entrada, Categoria


# Create your views here.

def blog(request):
    cargapost = Entrada.objects.all()
    # cargacat = Categoria.objects.distinct()
    
    return render(request, 'blogx/blog.html', {'post': cargapost})
    # return render(request, 'blogx/blog.html', {'post': cargapost, 'carcat': cargacat})

def catx(request, categoria_id):
    # FILTRA LA CATEGORÍA
    varcat = Categoria.objects.get(id=categoria_id)
    # MUESTRA LOS POSTS
    entradas = Entrada.objects.filter(categorias=varcat)
    

    return render(request, 'blogx/filtrada.html', {'lacatego': varcat, 'postca': entradas})
