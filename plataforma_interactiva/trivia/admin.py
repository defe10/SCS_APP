from django.contrib import admin
from .models import Pregunta, Opcion

class OpcionInline(admin.TabularInline): 
    model = Opcion
    extra = 3  # <---- cantidad de opciones de respuesta

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]
    list_display = ['texto']  # ajustalo si usás otro campo

admin.site.register(Pregunta, PreguntaAdmin)
