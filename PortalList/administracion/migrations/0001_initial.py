# Generated by Django 4.1.1 on 2022-10-01 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('cod_administrador', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('Contrasenia', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cedula', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('usuario', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('Contrasenia', models.CharField(max_length=255)),
                ('cod_administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.administrador')),
            ],
        ),
    ]