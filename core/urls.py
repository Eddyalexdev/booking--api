from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rooms/', include('room.urls')),
    path('api/bookings/', include('booking.urls')),
]
