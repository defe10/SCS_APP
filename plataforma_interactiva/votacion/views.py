from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Voto
from django.contrib.auth.decorators import login_required

@login_required
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    votos_usuario = Voto.objects.filter(usuario=request.user)
    peliculas_votadas = [v.pelicula_id for v in votos_usuario]
    return render(request, 'votacion/lista_peliculas.html', {
        'peliculas': peliculas,
        'peliculas_votadas': peliculas_votadas
    })








@login_required
def votar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    if request.method == 'POST':
        valor = request.POST.get('valor')
        if not Voto.objects.filter(usuario=request.user, pelicula=pelicula).exists():
            Voto.objects.create(usuario=request.user, pelicula=pelicula, valor=valor)
        return redirect('votacion:lista_peliculas')
    return render(request, 'votacion/votar_pelicula.html', {'pelicula': pelicula})

