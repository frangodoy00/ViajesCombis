# Generated by Django 3.2 on 2021-05-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0019_alter_viaje_ruta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]