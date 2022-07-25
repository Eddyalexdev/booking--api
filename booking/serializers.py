from rest_framework import serializers
from .models import Booking
from room.serializers import RoomSerializer

class BookingSerializer(serializers.ModelField):
    room = RoomSerializer()
    class Meta:
        model = Booking
        fields = ("id", "room", "days_stay", "amount", "method")
