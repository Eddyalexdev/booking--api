from django.db import models

# Create your models here.

class Room(models.Model):
    rooms_id = ( ("A1", "A1"), ("A2", "A2"), ("B1", "B1"), ("B2", "B2") )

    location_room = models.CharField(max_length=10, choices=rooms_id)
    description = models.TextField()
    avaiable = models.BooleanField(default=True)

    def __str__(self):
        return self.location_room

