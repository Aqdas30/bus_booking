# Generated by Django 5.1.6 on 2025-02-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0003_alter_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busroute',
            old_name='price',
            new_name='price_one_way',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='passengers',
        ),
        migrations.AddField(
            model_name='booking',
            name='adults',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='children',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='students',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='trip_type',
            field=models.CharField(choices=[('one_way', 'One Way'), ('return', 'Return')], default='one_way', max_length=10),
        ),
        migrations.AddField(
            model_name='busroute',
            name='country',
            field=models.CharField(choices=[('BA', 'Bosnia and Herzegovina'), ('HR', 'Croatia'), ('SI', 'Slovenia'), ('AT', 'Austria'), ('CH', 'Switzerland'), ('DE', 'Germany'), ('NL', 'Netherlands'), ('BE', 'Belgium')], default='BA', max_length=2),
        ),
        migrations.AddField(
            model_name='busroute',
            name='departure_days',
            field=models.CharField(blank=True, help_text="Comma separated days, e.g. 'Mon, Wed, Fri'", max_length=255),
        ),
        migrations.AddField(
            model_name='busroute',
            name='departure_times',
            field=models.CharField(blank=True, help_text="Comma separated times, e.g. '08:00, 14:00'", max_length=255),
        ),
        migrations.AddField(
            model_name='busroute',
            name='duration',
            field=models.PositiveIntegerField(default=0, help_text='Duration in minutes'),
        ),
        migrations.AddField(
            model_name='busroute',
            name='price_return',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
    ]
