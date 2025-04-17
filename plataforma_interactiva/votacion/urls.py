from django.urls import path
from . import views

app_name = 'votacion'

urlpatterns = [
    path('', views.lista_peliculas, name='lista_peliculas'),  # esta es la clave
    path('votar/<int:pelicula_id>/', views.votar_pelicula, name='votar_pelicula'),
]
