from django.db import models


class Agenda(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
