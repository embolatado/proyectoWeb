from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse('Pag. Inicio')


def servicios(request):
    return HttpResponse('Pag. Servicios')


def tienda(request):
    return HttpResponse('Pag. Tienda')


def blog(request):
    return HttpResponse('Pag. Blog')


def contacto(request):
    return HttpResponse('Pag. Contacto')


