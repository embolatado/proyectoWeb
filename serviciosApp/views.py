from django.shortcuts import render
from serviciosApp.models import Servicio

# Create your views here.

def servicios(request):
    cargador = Servicio.objects.all()

    return render(request, 'dienst/services.html', {"srvx": cargador})

