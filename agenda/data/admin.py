from django.contrib import admin
from .models import Contactos

# Register your models here.
class ProjetAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Contactos, ProjetAdmin)
