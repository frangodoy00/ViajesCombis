# Generated by Django 3.1.7 on 2021-04-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0005_user_fechadenaciemiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fechaDeNaciemiento',
            field=models.DateField(null=True),
        ),
    ]