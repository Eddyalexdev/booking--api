# Generated by Django 4.0.6 on 2022-07-25 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_stay', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('1', 'Pendiente'), ('2', 'Pagado'), ('3', 'Eliminado')], max_length=20)),
                ('amount', models.FloatField(default=0)),
                ('method', models.CharField(choices=[('1', 'Credit Card'), ('2', 'Paypal')], max_length=50)),
                ('room_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.room')),
            ],
        ),
    ]
