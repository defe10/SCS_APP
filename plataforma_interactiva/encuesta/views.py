from django.shortcuts import render, get_object_or_404, redirect
from .models import PreguntaEncuesta, VotoEncuesta
from django.contrib.auth.decorators import login_required

@login_required
def lista_preguntas(request):
    preguntas = PreguntaEncuesta.objects.all()
    votos_usuario = VotoEncuesta.objects.filter(usuario=request.user)
    preguntas_votadas = [v.pregunta_id for v in votos_usuario]
    return render(request, 'encuesta/lista_encuesta.html', {
        'preguntas': preguntas,
        'preguntas_votadas': preguntas_votadas
    })

@login_required
def votar(request, pregunta_id):
    pregunta = get_object_or_404(PreguntaEncuesta, id=pregunta_id)
    if request.method == 'POST':
        valor = request.POST.get('valor')
        if not VotoEncuesta.objects.filter(usuario=request.user, pregunta=pregunta).exists():
            VotoEncuesta.objects.create(usuario=request.user, pregunta=pregunta, valor=valor)
        return redirect('encuesta:lista_preguntas')
    return render(request, 'encuesta/votar_encuesta.html', {'pregunta': pregunta})

