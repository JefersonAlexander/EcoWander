from django.urls import path
from .views import Registro, log_in, log_out

urlpatterns = [
   
  
    path('',Registro.as_view(), name="authentication"),

    path('log_out',log_out, name="log_out"),

    path('log_in',log_in, name="log_in"),

    
]