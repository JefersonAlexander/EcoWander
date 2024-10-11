from django.urls import path
from .views import Register, log_in, log_out

urlpatterns = [
   
  
    path('',Register.as_view(), name="authentication"),

    path('log_out',log_out, name="log_out"),

    path('log_in',log_in, name="log_in"),

]