# Generated by Django 4.1.5 on 2023-01-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='sexe',
            field=models.CharField(blank=True, choices=[('h', 'Homme'), ('f', 'Femme')], max_length=1, null=True),
        ),
    ]