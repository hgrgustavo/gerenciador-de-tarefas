
from django.db import models


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("baixa", "Baixa"), 
        ("media", "Média"),
        ("alta", "Alta"),
    ]
    
    STATUS_CHOICES = [
        ("a fazer", "A Fazer"),
        ("fazendo", "Fazendo"), 
        ("pronto", "Pronto"),
    ]
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    descricao = models.CharField(max_length=255)
    setor = models.CharField(max_length=255)
    prioridade = models.CharField(max_length=5, choices=PRIORIDADE_CHOICES)
    data_cadastro = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="a fazer")

    class Meta:
        managed = False
        db_table = 'tarefa'


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usuario'
