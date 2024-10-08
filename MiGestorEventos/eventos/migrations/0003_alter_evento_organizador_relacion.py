# Generated by Django 5.1 on 2024-09-09 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0002_alter_evento_fecha"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evento",
            name="organizador_relacion",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eventos.organizador",
            ),
        ),
    ]
