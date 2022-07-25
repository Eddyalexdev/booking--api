from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bookings),
    path('create', views.create_booking)
]
