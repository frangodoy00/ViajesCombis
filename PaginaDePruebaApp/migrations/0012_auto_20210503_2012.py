# Generated by Django 3.2 on 2021-05-03 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0011_auto_20210503_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='enCurso',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
    ]