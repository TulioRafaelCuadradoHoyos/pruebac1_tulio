from django.db import models




# Create your models here.

class Equipo(models.Model):
    Fecha       = models.DateField()
    Descripcion = models.CharField(max_length=50)
    Resultado   = models.BooleanField()


    def __str__(self):
        return self.Descripcion



