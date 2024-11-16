import uuid
from django.db import models
from tour.models import Tour
from authentication.models import UserProfile

class Reservation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()  # Agregar este campo para la fecha seleccionada
    people_count = models.IntegerField(default=1)  # Agregar este campo para el número de personas
    price_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pendiente'), ('confirmed', 'Confirmada'), ('cancelled', 'Cancelada')],
        default='pending'
    )
    created = models.DateTimeField(auto_now_add=True)
    confirmation_code = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = str(uuid.uuid4()).split('-')[0]  # Genera un código único para cada reserva
        super().save(*args, **kwargs)