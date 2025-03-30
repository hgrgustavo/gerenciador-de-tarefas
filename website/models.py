
from django.db import models


class Tarefa(models.Model):
    CHOICES_PRIORIDADE = [
        ("baixa", "Baixa"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    CHOICES_STATUS = [
        ("a fazer", "A fazer"),
        ("fazendo", "Fazendo"),
        ("pronto", "Pronto"),
    ]

    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    descricao = models.TextField()
    setor = models.CharField(max_length=255)
    prioridade = models.CharField(max_length=5, choices=CHOICES_PRIORIDADE)
    data_cadastro = models.DateField()
    status = models.CharField(
        max_length=7, choices=CHOICES_STATUS, default="a fazer")

    class Meta:
        db_table = 'tarefa'
        unique_together = (('id', 'usuario'),)


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'usuario'
