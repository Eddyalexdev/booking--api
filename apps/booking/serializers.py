from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelField):
    class Meta:
        model = Booking
        fields = ( "__all__" )
