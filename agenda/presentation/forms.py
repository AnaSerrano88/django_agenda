from django import forms
from data import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contactos
        fields = ('nombre','segundo_nombre', 'apellido_paterno','apellido_materno','tel_casa','celular','email','twitter','web_page')


   