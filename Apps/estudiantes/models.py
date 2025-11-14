from django.db import models

class Estudiante(models.Model):
	nombre = models.CharField(max_length=100)
	apellido= models.CharField(max_length=100)
	creacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
        	return f"{self.nombre}"