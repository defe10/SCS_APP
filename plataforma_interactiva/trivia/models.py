from django.db import models

class Pregunta(models.Model):
    texto = models.CharField("Pregunta", max_length=255)

    def __str__(self):
        return self.texto

class Opcion(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        related_name='opciones',
        on_delete=models.CASCADE
    )
    texto = models.CharField("Opción", max_length=255)
    es_correcta = models.BooleanField("¿Es correcta?", default=False)

    def __str__(self):
        return self.texto

