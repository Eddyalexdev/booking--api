# Generated by Django 4.0.6 on 2022-07-25 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('booking', '0002_alter_booking_method_alter_booking_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='billing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.billing'),
        ),
    ]
