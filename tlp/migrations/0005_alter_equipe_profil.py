# Generated by Django 4.1 on 2022-09-30 21:06

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlp', '0004_alter_equipe_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='Profil',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\PythonDev\\Projects\\first_app\\media'), upload_to=''),
        ),
    ]
