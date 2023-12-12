from django.db import models

class Socios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Actividades(models.Model):
    nombre_actividad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Sedes(models.Model):
    nombre_sede = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

