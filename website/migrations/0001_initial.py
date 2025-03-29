# Generated by Django 4.2.20 on 2025-03-29 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "db_table": "usuario",
            },
        ),
        migrations.CreateModel(
            name="Tarefa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.TextField()),
                ("setor", models.CharField(max_length=255, unique=True)),
                (
                    "prioridade",
                    models.CharField(
                        choices=[
                            ("baixa", "Baixa"),
                            ("media", "Media"),
                            ("alta", "Alta"),
                        ],
                        max_length=5,
                    ),
                ),
                ("data_cadastro", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("a fazer", "A fazer"),
                            ("fazendo", "Fazendo"),
                            ("pronto", "Pronto"),
                        ],
                        default="a fazer",
                        max_length=7,
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="website.usuario",
                    ),
                ),
            ],
            options={
                "db_table": "tarefa",
                "unique_together": {("id", "usuario")},
            },
        ),
    ]
