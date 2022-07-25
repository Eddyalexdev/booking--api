from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#booking
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
@api_view(['GET'])
def get_bookings(request):
    if Booking.objects.all().exists():
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({ "bookings": serializer.data }, status=status.HTTP_200_OK)
    return Response({ "error": "No se encontraron Reservas" }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_bookings(request):
    data = request.data
    room = data['room']
    is_avaiable = room.avaiable

    #validations
    if not is_avaiable:
        Response({ "error": "El Cuarto no esta disponible" }, status = status.HTTP_400_BAD_REQUEST)
    if not id:
        return  Response({ "error": "No se realizo la reserva debido a que no se encuentra el id" }, status=status.HTTP_400_BAD_REQUEST)

    #save data
    serializer = BookingSerializer()
    
    if serializer.is_valid():
        serializer.save()
    return Response({ "error": "No se realizo la reserva" }, status=status.HTTP_400_BAD_REQUEST)
