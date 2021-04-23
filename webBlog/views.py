from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'webBlog/index.html')


def servicios(request):
    return render(request, 'webBlog/services.html')


def tienda(request):
    return render(request, 'webBlog/store.html')


def blog(request):
    return render(request, 'webBlog/blog.html')


def contacto(request):
    return render(request, 'webBlog/contact.html')



