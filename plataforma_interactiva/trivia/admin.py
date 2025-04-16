from django.contrib import admin
from .models import Pregunta, Opcion

class OpcionInline(admin.TabularInline):  # o admin.StackedInline si preferís
    model = Opcion
    extra = 3  # cuántas opciones vacías aparecen por defecto

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]
    list_display = ['texto']  # ajustalo si usás otro campo

admin.site.register(Pregunta, PreguntaAdmin)
