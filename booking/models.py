from django.db import models

#imports other apps
from room.models import Room

# Create your models here.
class Booking(models.Model):
    #choices
    payment_methods = (("1", "Credit Card"), ("2", "Paypal"))
    state_room = (("1", "Pendiente"), ("2", "Pagado"), ("3", "Eliminado"))

    #billing details


    #details
    room_details = models.ForeignKey(Room, related_name="room", on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    days_stay = models.IntegerField(default=0)
    state = models.CharField(max_length=20, choices =state_room)

    #payment
    amount = models.FloatField(default=0)
    method = models.CharField(max_length=50, choices=payment_methods)
