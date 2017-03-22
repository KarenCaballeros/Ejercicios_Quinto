from django.shortcuts import render
from grados.models import Grado


def lista_grados(request):
	grados = Grado.objects.all()
	return render(request, 'lista_grados.html',
		{'grados' : grados})
