# Generated by Django 4.1.1 on 2022-10-24 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_grupo_alumnos_tienen_codprofesor_pasan_codlista_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='codAdministrador',
        ),
    ]