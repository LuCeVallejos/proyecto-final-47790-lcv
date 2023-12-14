from django.db import models


class Socio(models.Model):
    dni = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField()

    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellido}"


class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Sede(models.Model):
    nombre_sede = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

