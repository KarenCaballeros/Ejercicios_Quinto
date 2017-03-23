from django.shortcuts import render
from grados.models import Grado


def lista_grados(request):
	grados = Grado.objects.all()
	return render(request, 'lista_grados.html',
		{'grados' : grados})

def detalle_grado(request, grado_pk):
	grado = Grado.objects.grado_pk()
	return render(request, 'detalle_grado.html',
		{'estudiantes' : estudiantes})
