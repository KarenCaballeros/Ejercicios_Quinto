from django.db import models

class Estudiante(models.Model):
	nombres = models.CharField(max_length = 100)
	apellidos = models.CharField(max_length = 100)
	edad = models.IntegerField(default= 0)
	grado = models.ForeignKey("grados.Grado" )
		
	def __str__(self):
		return "%s %s - %s" % (
			self.nombres,
			self.apellidos,
			self.grado)

