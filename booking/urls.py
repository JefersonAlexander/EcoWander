from django.urls import path

from . import views


urlpatterns = [
   
    
    path('booking/<int:tour_id>/',views.booking, name="Booking"),
    path('showbooking/', views.show_booking, name="ShowBooking"),
]