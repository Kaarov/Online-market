# Generated by Django 3.2 on 2022-08-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_auto_20220824_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
