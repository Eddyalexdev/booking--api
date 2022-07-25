from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#booking
from .models import Booking
from room.models import Room 
from room.serializers import RoomSerializer
from billing.models import Billing
from .serializers import BookingSerializer

# Create your views here.
@api_view(['GET'])
def get_bookings(request):
    if Booking.objects.all().exists():
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({ "bookings": serializer.data }, status=status.HTTP_200_OK)
    return Response({ "error": "no se encontraron reservas" }, status=400)

@api_view(['POST'])
def create_booking(request):
    data = request.data
    id_room = data['room']
    room = Room.objects.filter(id = id_room).first()

    print(id_room)
    #validations
    if not room.avaiable or not id_room:
        Response({ "error": "No se realizo la reserva" }, status=status.HTTP_400_BAD_REQUEST)

    print(room.avaiable)
    RoomSerializer(room.avaiable, False)

    #save data
    serializer = BookingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ "booking" : serializer.data }, status=status.HTTP_200_OK)
    return Response({ "error": "No se realizo la reserva" }, status=status.HTTP_400_BAD_REQUEST)

