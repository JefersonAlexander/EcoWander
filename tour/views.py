from django.shortcuts import get_object_or_404, render
from .models import Tour


# Create your views here.
def tour(request):    
    tours=Tour.objects.all()
    return render(request, "tour/tour.html", {"tours":tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour/tourDetail.html', {'tour': tour})

