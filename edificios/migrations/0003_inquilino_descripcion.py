# Generated by Django 4.1.4 on 2023-01-17 00:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edificios', '0002_encargado'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquilino',
            name='descripcion',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
