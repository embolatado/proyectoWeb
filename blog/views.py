from django.shortcuts import render
from .models import Entrada


# Create your views here.

def blog(request):
    cargapost = Entrada.objects.all()
    return render(request, 'blogx/blog.html', {'post': cargapost})

