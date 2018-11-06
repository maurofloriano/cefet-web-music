from django.db import models

# Create your models here.

class EstiloMusical(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome


class Banda(models.Model):
    nome = models.TextField()
    email = models.EmailField()
    site = models.URLField()
    numero_membros = models.IntegerField()
    estilo = models.ForeignKey(EstiloMusical, on_delete = models.PROTECT)

    def __str__(self):
        return self.nome

class Musico(models.Model):
    nome = models.TextField()
    email = models.EmailField()
    artista_solo = models.BooleanField()
    bandas = models.ManyToManyField(Banda)

    def __str__(self):  
        return self.nome

