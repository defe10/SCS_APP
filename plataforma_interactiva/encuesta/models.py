from django.db import models
from django.contrib.auth.models import User

class PreguntaEncuesta(models.Model):
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

class VotoEncuesta(models.Model):
    OPCIONES = [
        ('1', 'No estoy de acuerdo'),
        ('2', 'Neutral'),
        ('3', 'Estoy de acuerdo'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votos_encuesta')
    pregunta = models.ForeignKey(PreguntaEncuesta, on_delete=models.CASCADE, related_name='votos')
    valor = models.CharField(max_length=1, choices=OPCIONES)

    class Meta:
        unique_together = ('usuario', 'pregunta')

    def __str__(self):
        return f'{self.usuario.username} votó {self.get_valor_display()} en "{self.pregunta}"'
