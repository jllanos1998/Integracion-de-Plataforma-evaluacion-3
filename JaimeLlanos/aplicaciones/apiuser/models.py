from pyexpat import model
from django.db import models

# Create your models here.
class Jaime(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ) 
    id_user = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=120)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.nombre