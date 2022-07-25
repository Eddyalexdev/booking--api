from django.db import models
from room.models import Room

# Create your models here.
class Billing(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    billing_number = models.IntegerField()
    emision_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.billing_number

