from django.db import models

#imports other apps
from room.models import Room

# Create your models here.
class Booking(models.Model):
    payment_methods = (("1", "Credit Card"), ("2", "Paypal"))

    #details
    room_details = models.ForeignKey(Room, related_name="room", on_delete=models.CASCADE)
    days_stay = models.IntegerField(default=0)

    #payment
    amount = models.FloatField(default=0)
    method = models.CharField(max_length=50, choices=payment_methods)
