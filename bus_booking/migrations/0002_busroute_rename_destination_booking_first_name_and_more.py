# Generated by Django 5.1.6 on 2025-02-21 10:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='destination',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_reference',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='last_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='route',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bus_booking.busroute'),
        ),
    ]
