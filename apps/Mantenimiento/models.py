from django.db import models
from django.db.models.deletion import CASCADE
from apps.Equipo.models import Equipo




# Create your models here.

class Mantenimiento(models.Model):

    Marca  = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)


    def __str__(self):
        return self.Modelo

