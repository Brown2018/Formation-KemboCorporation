# Generated by Django 4.1 on 2022-09-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Libellé', models.CharField(max_length=20)),
                ('Commentaires', models.TextField()),
            ],
        ),
    ]
