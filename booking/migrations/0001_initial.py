# Generated by Django 3.2 on 2022-12-04 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingPole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('time_6_7', models.BooleanField(default=True, verbose_name='6 : 7')),
                ('time_7_8', models.BooleanField(default=True, verbose_name='7 : 8')),
                ('time_8_9', models.BooleanField(default=True, verbose_name='8 : 9')),
                ('time_9_10', models.BooleanField(default=True, verbose_name='9 : 10')),
                ('time_10_11', models.BooleanField(default=True, verbose_name='10 : 11')),
                ('time_11_12', models.BooleanField(default=True, verbose_name='11 : 12')),
                ('time_12_13', models.BooleanField(default=True, verbose_name='12 : 13')),
                ('time_13_14', models.BooleanField(default=True, verbose_name='13 : 14')),
                ('time_14_15', models.BooleanField(default=True, verbose_name='14 : 15')),
                ('time_15_16', models.BooleanField(default=True, verbose_name='15 : 16')),
                ('time_16_17', models.BooleanField(default=True, verbose_name='16 : 17')),
                ('time_17_18', models.BooleanField(default=True, verbose_name='17 : 18')),
                ('time_18_19', models.BooleanField(default=True, verbose_name='18 : 19')),
                ('time_19_20', models.BooleanField(default=True, verbose_name='19 : 20')),
                ('time_20_21', models.BooleanField(default=True, verbose_name='20 : 21')),
                ('time_21_22', models.BooleanField(default=True, verbose_name='21 : 22')),
                ('time_22_23', models.BooleanField(default=True, verbose_name='22 : 23')),
                ('time_23_24', models.BooleanField(default=True, verbose_name='23 : 24')),
            ],
            options={
                'verbose_name': 'BookingPole',
                'verbose_name_plural': 'BookingPoles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BookingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_from', models.IntegerField(verbose_name='Check In')),
                ('time_to', models.IntegerField(verbose_name='Check Out')),
            ],
            options={
                'verbose_name': 'BookingTime',
                'verbose_name_plural': 'BookingTimes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BookingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="Student's Name")),
                ('booking_day', models.DateField(verbose_name='Booking Day')),
                ('booking_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='booking.bookingpole')),
                ('booking_time', models.ManyToManyField(related_name='times', to='booking.BookingTime')),
            ],
            options={
                'verbose_name': 'BookingItem',
                'verbose_name_plural': 'BookingItems',
                'ordering': ['id'],
            },
        ),
    ]