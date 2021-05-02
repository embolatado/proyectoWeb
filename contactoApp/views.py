from django.shortcuts import render, redirect
from .forms import FormKontakt

# Create your views here.

def contacto(request):

    el_formulario = FormKontakt()

    if request.method == "POST":
        el_formulario = FormKontakt(data=request.POST)

        if el_formulario.is_valid():
            var_nom = request.POST.get("visita")
            var_crr = request.POST.get("correo")
            var_msj = request.POST.get("mensaj")

            # REDIRECCIONAR A URL POR GET DESPUÉS DE DETECTAR EL POST
            return redirect("/contacto/?gracias")

    return render(request, 'contacta/contact.html', {"miformulario": el_formulario})
