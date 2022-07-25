from rest_framework import serializers
from .models import Booking
from room.serializers import RoomSerializer
from billing.serializers import BillingSerializer

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    billing = BillingSerializer()

    class Meta:
        model = Booking
        fields = ("id", "room", "billing", "user", "days_stay", "amount", "method")
