from django.shortcuts import render, get_object_or_404, redirect
from .models import Pregunta



def comenzar_trivia(request):        
    request.session['score'] = 0
    request.session['total'] = 0

    primera = Pregunta.objects.order_by('id').first()   

    if primera is None:
        return render(request, 'trivia/trivia.html', {
            'estado': 'sin_preguntas'
        })

    return redirect('trivia:pregunta', pregunta_id=primera.id)







def pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    opciones = pregunta.opciones.all()

    if request.method == 'POST':
        opcion_id = request.POST.get('opcion')
        seleccion = pregunta.opciones.filter(id=opcion_id).first()
        correcta = bool(seleccion and seleccion.es_correcta)

        request.session['total'] += 1
        if correcta:
            request.session['score'] += 1

        siguiente = Pregunta.objects.filter(id__gt=pregunta.id).order_by('id').first()


        mensaje_error = ""  #<---mensaje para pregunta incorrecta
        if not correcta:
            mensaje_error = pregunta.mensaje_error or ""

        if siguiente:
            return render(request, 'trivia/trivia.html', {
                'estado': 'resultado',
                'correcta': correcta,
                'siguiente_id': siguiente.id,
                'mensaje_error': mensaje_error,  # <--- lo manda al template
            })
        else:
            return redirect('trivia:resumen')

    return render(request, 'trivia/trivia.html', {
        'estado': 'pregunta',
        'pregunta': pregunta,
        'opciones': opciones,
    })








def resumen(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)
    return render(request, 'trivia/trivia.html', {
        'estado': 'resumen',
        'score': score,
        'total': total,
    })

