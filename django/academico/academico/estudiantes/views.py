from django.shortcuts import render
from estudiantes.models import Estudiante

def lista_estudiantes(request):
	estudiantes = Estudiante.objects.all()
	return render(request, 'lista_estudiantes.html',
		{'estudiantes' : estudiantes})
