# Generated by Django 4.1.5 on 2023-01-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=160)),
                ('encargado', models.CharField(max_length=32)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inquilino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('edificio', models.CharField(max_length=30)),
            ],
        ),
    ]
