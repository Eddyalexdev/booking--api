from django.db import models
from room.models import Room

# Create your models here.
class Billing(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    billing_number = models.IntegerField(default=0)
    emision_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} Room - in date {}".format(self.room, self.emision_date)
