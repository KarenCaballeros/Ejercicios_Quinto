from django.db import models

class Estudiante(models.Model):
	nombres = models.CharField(max_length = 100)
	apellidos = models.CharField(max_length = 100)
	edad = models.IntegerField(defaul= 0)
	grado = models.ForeignKey("grados.Grado" )
		
	def _unicode_(self):
		return "%S %S - %S" % (
			self.nombres
			self.apellidos
			self.grado)

