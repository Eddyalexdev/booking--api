from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rooms/', include('apps.room.urls')),
    path('api/bookings/', include('apps.booking.urls')),
]
