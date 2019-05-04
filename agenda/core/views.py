from django.shortcuts import render, HttpResponse, redirect
from data import models
from presentation import forms
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'presentation/home.html')

def agenda(request):
    contactos = models.Contactos.objects.all()
    return render(request, 'presentation/agenda.html',{'contactos': contactos})
"""
def newcontacto(request):
    contactForm = forms.ContactForm()

    if request.method == 'POST':
        contactForm = forms.ContactForm(request.POST, request.FILES)
        if contactForm.is_valid():
            contactForm.save()
            return redirect(reverse('agenda'))

    return render(request, 'presentation/contacto.html',{'form':contactForm})
"""
class nuevocontacto(CreateView):
    model=models.Contactos
    fields='__all__'
    template_name="presentation/contactos.html"
    def get_success_url(self):
        return reverse_lazy("agenda")

def buscar(request, name):
    return render(request,'presentation/uncontacto.html')
















































