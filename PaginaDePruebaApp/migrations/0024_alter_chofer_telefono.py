# Generated by Django 3.2 on 2021-05-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0023_alter_chofer_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='telefono',
            field=models.PositiveIntegerField(max_length=10, null=True),
        ),
    ]
