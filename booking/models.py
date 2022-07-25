from django.db import models

#imports other apps
from room.models import Room
from billing.models import Billing
from user.models import User

# Create your models here.
class Booking(models.Model):
    #choices
    payment_methods = (("CC", "Credit Card"), ("PP", "Paypal"))
    state_room = (("PE", "Pendiente"), ("PA", "Pagado"), ("EL", "Eliminado"))

    #billing details
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    #details
    room_details = models.ForeignKey(Room, related_name="room", on_delete=models.CASCADE)
    days_stay = models.IntegerField(default=0)
    state = models.CharField(max_length=20, choices =state_room)

    #payment
    amount = models.FloatField(default=0)
    method = models.CharField(max_length=50, choices=payment_methods)
