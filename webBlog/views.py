from django.shortcuts import render, HttpResponse

from serviciosApp.models import Servicio

# Create your views here.

def inicio(request):
    return render(request, 'webBlog/index.html')


def servicios(request):
    cargador = Servicio.objects.all()

    return render(request, 'webBlog/services.html', {"srvx": cargador})


def tienda(request):
    return render(request, 'webBlog/store.html')


def blog(request):
    return render(request, 'webBlog/blog.html')


def contacto(request):
    return render(request, 'webBlog/contact.html')



