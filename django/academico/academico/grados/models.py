from django.db import models

class Grado(models.Model):
	nombre = models.CharField(max_length = 100)
	orden = models.IntegerField(default= 0)

	def __str__(self):
		return self.nombre