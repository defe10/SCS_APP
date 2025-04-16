from django.urls import path
from . import views

app_name = 'trivia'

urlpatterns = [
    path('', views.comenzar_trivia, name='comenzar'),
    path('pregunta/<int:pregunta_id>/', views.pregunta, name='pregunta'),
    path('resumen/', views.resumen, name='resumen'),
]

