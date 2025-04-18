from django.shortcuts import render, get_object_or_404, redirect
from .models import PreguntaEncuesta, VotoEncuesta
from django.contrib.auth.decorators import login_required

@login_required
def lista_preguntas(request):             #<-----listas de preguntas con votos (realizados o no) y saber si ya fue votada o no por el usuario
    preguntas = PreguntaEncuesta.objects.all()
    votos_usuario = VotoEncuesta.objects.filter(usuario=request.user)
    preguntas_votadas = [v.pregunta_id for v in votos_usuario]
    return render(request, 'encuesta/lista_encuesta.html', {
        'preguntas': preguntas,
        'preguntas_votadas': preguntas_votadas
    })






@login_required
def votar(request, pregunta_id):
    pregunta = get_object_or_404(PreguntaEncuesta, id=pregunta_id)   #<----- busca lista de pelis o mara error 404
    if request.method == 'POST':  # <---- cuando el usuario vota envía formulario, se accede (request.POST.get) y se extae el valor el valor
        valor = request.POST.get('valor')
        if not VotoEncuesta.objects.filter(usuario=request.user, pregunta=pregunta).exists():  #<-----si ya votó no hace nada, sino crea VotoEncuesta 
            VotoEncuesta.objects.create(usuario=request.user, pregunta=pregunta, valor=valor)
        return redirect('encuesta:lista_preguntas')
    return render(request, 'encuesta/votar_encuesta.html', {'pregunta': pregunta})

