# Generated by Django 4.1.2 on 2022-10-23 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0002_grupo_rename_contrasenia_administrador_contraseña_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('codLista', models.IntegerField(primary_key=True, serialize=False)),
                ('falta', models.BooleanField(default=False)),
                ('justificada', models.BooleanField(default=False)),
                ('llegada_tarde', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('codProfesor', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('cargo', models.CharField(max_length=255)),
                ('antiguedad', models.CharField(max_length=255)),
                ('cedula', models.IntegerField(unique=True)),
                ('usuario', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('codadministrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.administrador')),
                ('usuarioci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codMateria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('horario', models.IntegerField()),
                ('cod_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesores.profesor')),
            ],
        ),
    ]
