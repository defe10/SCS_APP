from django.db import models

class Pregunta(models.Model):
    texto = models.CharField("Pregunta", max_length=255)
    mensaje_error = models.TextField("Mensaje si responde mal", blank=True, null=True)  # <---- mensaje por si la respuesta es incorrecta

    def __str__(self):
        return self.texto

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField("Opción", max_length=255)
    es_correcta = models.BooleanField("¿Es correcta?", default=False)

    def __str__(self):
        return self.texto



# CharField: guarda texto hasta 255 caracteres 
# TextField: textos más largos
# ForeignKey: para opciones
# BooleanField: para VoF