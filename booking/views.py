from django.shortcuts import render, redirect, get_object_or_404
from tour.models import Tour
from .forms import ReservationForm
from authentication.models import UserProfile
from django.contrib.auth.decorators import login_required
from .models import Reservation

def booking(request, tour_id):
    user_profile = request.user
    tour = get_object_or_404(Tour, id=tour_id)  # Obtiene el tour usando el id proporcionado en la URL

    # Recuperar los parámetros de la URL
    people_count = request.GET.get('people_count', 1)  # Valor por defecto es 1
    total_price = request.GET.get('total_price', tour.price)  # Valor por defecto es el precio del tour
    date = request.GET.get('date', None)  # Si no hay fecha seleccionada, no se pasa

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reserva = form.save(commit=False)  # Crea una instancia sin guardarla en la BD
            reserva.user = user_profile       # Asigna el usuario autenticado
            reserva.tour = tour               # Asigna el tour obtenido de la URL
            reserva.date = date               # Fecha seleccionada
            reserva.people_count = people_count  # Número de personas
            reserva.price_total = total_price  # Precio total
            reserva.save()                    # Guarda la reserva con los campos asignados
            return redirect('ShowBooking')   # Redirige a una página de confirmación o éxito
    else:
        form = ReservationForm(initial={
            'people_count': people_count,
            'price_total': total_price,
            'date': date
        })

    return render(request, 'booking/booking.html', {
        'form': form,
        'user_profile': user_profile,
        'tour': tour,
        'people_count': people_count,
        'total_price': total_price,
        'date': date
    })


@login_required
def show_booking(request):
    # Obtener las reservas del usuario autenticado
    user_reservations = Reservation.objects.filter(user=request.user).order_by('-created')

    # Renderizar la página con las reservas del usuario
    return render(request, 'booking/showBooking.html', {'reservations': user_reservations})