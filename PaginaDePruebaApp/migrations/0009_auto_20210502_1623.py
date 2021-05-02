# Generated by Django 3.2 on 2021-05-02 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0008_auto_20210502_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combi',
            name='cantAsientosDisponibles',
        ),
        migrations.AlterField(
            model_name='combi',
            name='cantAsientos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='combi',
            name='chofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaDePruebaApp.chofer'),
        ),
        migrations.AlterField(
            model_name='combi',
            name='patente',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
