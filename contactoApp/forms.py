from django import forms

class FormKontakt(forms.Form):
    visita = forms.CharField(label="Nombre", max_length=50, required=False)
    correo = forms.EmailField(label="Correo", required=True,)
    mensaj = forms.CharField(widget=forms.Textarea, max_length=240, required=True, label="Mensaje") 