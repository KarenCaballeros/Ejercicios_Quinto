from django.db import models

class Grado(models.Model):
	nombre = models.CharField(max_length = 100)
	orden = models.IntegerField(defaul= 0)
		
