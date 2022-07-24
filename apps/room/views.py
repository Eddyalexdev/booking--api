from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Room
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
@api_view(['GET'])
def getRooms(request):
    if Room.objects.all().exists():
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({ "rooms": serializer.data }, status=status.HTTP_200_OK)
    return Response({ "error": "Error al cargar las habitaciones" }, status=status.HTTP_400_BAD_REQUEST)
