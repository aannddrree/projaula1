from django.db import models


class Tipo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Agenda(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    tipo = models.OneToOneField(Tipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descricao
