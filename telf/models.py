from django.db import models

class Celular(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ram = models.IntegerField()
    pantalla= models.CharField(max_length=100)
