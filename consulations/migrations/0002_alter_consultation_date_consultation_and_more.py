# Generated by Django 4.1.5 on 2023-01-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='date_consultation',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
