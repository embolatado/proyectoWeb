from django.shortcuts import render, redirect
from .forms import FormKontakt
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def contacto(request):

    el_formulario = FormKontakt()

    if request.method == "POST":
        el_formulario = FormKontakt(data=request.POST)

        if el_formulario.is_valid():
            var_nom = request.POST.get("visita")
            var_crr = request.POST.get("correo")
            var_msj = request.POST.get("mensaj")
            
            betreff = "Mensaje desde Blog Contacto de " + var_nom
            nachricht = var_msj + " :: " + var_crr
            email_desde = settings.EMAIL_HOST_USER
            email_para = ['embolatado@gmail.com']
            send_mail(betreff, nachricht, email_desde, email_para)
            # REDIRECCIONAR A URL POR GET DESPUÉS DE DETECTAR EL POST
            return redirect("/contacto/?gracias")

    return render(request, 'contacta/contact.html', {"miformulario": el_formulario})
