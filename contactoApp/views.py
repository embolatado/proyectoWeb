from django.shortcuts import render, redirect
from .forms import FormKontakt
from django.conf import settings
from django.core.mail import EmailMessage

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
            
            var_e = EmailMessage("Mensaje App Blog", "Mensaje de {} desde {} que dice:\n\n {}".format(var_nom, var_crr, var_msj), "", email_para, reply_to=["respuesta@email.com"])
            
            try:
                var_e.send()
                return redirect("/contacto/?gracias")
            except:
                return redirect("/contacto/?error")

    return render(request, 'contacta/contact.html', {"miformulario": el_formulario})
