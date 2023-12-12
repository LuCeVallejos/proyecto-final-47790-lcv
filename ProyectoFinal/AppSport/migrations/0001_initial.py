# Generated by Django 4.2.7 on 2023-12-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actividad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sedes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
