from django.db import models
from django.contrib.auth.models import User

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Voto(models.Model):
    OPCIONES_VOTO = [
        ('1', 'No me gustó'),
        ('2', 'Me gustó poco'),
        ('3', 'Me gustó'),
        ('4', 'Me gustó mucho'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    valor = models.CharField(max_length=1, choices=OPCIONES_VOTO)

    class Meta:
        unique_together = ('usuario', 'pelicula')  # Solo un voto por usuario por película

    def __str__(self):
        return f'{self.usuario.username} votó {self.get_valor_display()} a {self.pelicula.titulo}'

