# Generated by Django 4.1.5 on 2023-01-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rts", "0003_solicitart_cnpj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solicitart",
            name="cnpj",
            field=models.CharField(max_length=14),
        ),
    ]