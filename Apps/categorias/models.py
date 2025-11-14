from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(
        max_length=100,
        unique=True,  
        verbose_name='Nombre de la Categoría'
    )
    descripcion = models.TextField(
        blank=True,    
        null=True,     
        verbose_name='Descripción'
    )
    
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre'] 

    def __str__(self):
        return self.nombre