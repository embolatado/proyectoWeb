from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'webBlog/index.html')


def tienda(request):
    return render(request, 'webBlog/store.html')

'''
def contacto(request):
    return render(request, 'webBlog/contact.html')
'''
