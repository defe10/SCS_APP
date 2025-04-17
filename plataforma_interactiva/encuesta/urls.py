from django.urls import path
from . import views

app_name = 'encuesta'  

urlpatterns = [
    path('', views.lista_preguntas, name='lista_preguntas'),
    path('votar/<int:pregunta_id>/', views.votar, name='votar'),
]

