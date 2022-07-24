from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#booking
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
@api_view(['GET'])
def getBookings(request):
    if Booking.objects.all().exists()
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({ "bookings": serializer.data }, status=status.HTTP_200_OK)
    return Response({ "error": "No se encontraron Reservas" }, status=status.HTTP_400_BAD_REQUEST)
