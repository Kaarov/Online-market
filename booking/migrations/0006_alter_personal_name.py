# Generated by Django 3.2 on 2022-12-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20221207_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Name'),
        ),
    ]
