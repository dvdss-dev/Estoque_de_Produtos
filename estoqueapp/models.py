from django.db import models

# Create your models here.

class Itens(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)
    qnt = models.IntegerField()