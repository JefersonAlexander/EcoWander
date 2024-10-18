from django.shortcuts import render
from tour.models import Tour

# Create your views here.
def home(request):
    tours=Tour.objects.all()
    return render(request, "ecoWanderApp/home.html",{"tours":tours})
