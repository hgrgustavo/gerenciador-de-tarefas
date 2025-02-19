from django.db import models



class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuario'
          
    def __str__(self):
        return self.nome


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
        db_table = 'tarefa'
