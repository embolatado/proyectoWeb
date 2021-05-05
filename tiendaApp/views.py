from django.shortcuts import render
from .models import categoriaProducto, Producto

# Create your views here.

def tienda(request):
    
    var_prods = Producto.objects.all()
    
    return render(request, 'storeApp/store.html', {"prods": var_prods})
