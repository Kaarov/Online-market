# Generated by Django 3.2 on 2022-12-07 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingitem',
            name='booking_time',
        ),
        migrations.AddField(
            model_name='bookingitem',
            name='booking_time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='times', to='booking.bookingtime'),
            preserve_default=False,
        ),
    ]