# Generated by Django 3.2 on 2021-06-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0015_alter_viaje_imprevisto'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitado',
            name='suspendido',
            field=models.BooleanField(default=False),
        ),
    ]