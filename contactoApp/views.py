from django.shortcuts import render
from .forms import FormKontakt
# Create your views here.

def contacto(request):

    el_formulario = FormKontakt()

    return render(request, 'contacta/contact.html', {"miformulario": el_formulario})
