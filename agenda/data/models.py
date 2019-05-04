from django.db import models


# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20, blank=True)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    tel_casa = models.CharField(blank=True, max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    twitter = models.CharField(null=True,blank=True,max_length=30)
    web_page = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)   #guardar el registro cuando se inserta
    updated = models.DateTimeField(auto_now=True)       #guardar el registro cada que se modifica

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering =  ['apellido_paterno']

    def __str__(self):
        return self.apellido_paterno + " " + self.nombre