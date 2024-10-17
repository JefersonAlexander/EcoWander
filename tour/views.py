from django.shortcuts import get_object_or_404, render

from tour.forms import BusquedaTourForm
from .models import Tour


# Create your views here.
def tour(request):
    form = BusquedaTourForm(request.GET or None)    
    tours=Tour.objects.all()

    if form.is_valid():
        category= form.cleaned_data.get('category')
        deparment = form.cleaned_data.get('deparment')
        municipality=form.cleaned_data.get('municipality')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if category:
            tours = tours.filter(categories=category)
        if deparment:
            tours = tours.filter(deparment=deparment)
        if municipality:
            tours = tours.filter(municipality=municipality)
        if price_min is not None:
            tours = tours.filter(price__gte=price_min)
        if price_max is not None:
            tours = tours.filter(price__lte=price_max)

    return render(request, "tour/tour.html", {'form': form, "tours":tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour/tourDetail.html', {'tour': tour})

