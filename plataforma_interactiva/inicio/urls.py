
from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.menu_inicio, name='menu_inicio'),  # <--- este nombre en el template
]
