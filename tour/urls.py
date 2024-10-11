from django.urls import path

from .import views


urlpatterns = [
   
   
    path('',views.tour, name="Tour"),
    path('tour_detail/<int:tour_id>/',views.tour_detail, name="Tour_detail"),
      
]