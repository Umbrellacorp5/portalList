# Generated by Django 4.1.1 on 2022-11-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_rename_apellido_alumno_fotoalumno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fotoAlumno',
            field=models.ImageField(upload_to='Alumno'),
        ),
    ]
