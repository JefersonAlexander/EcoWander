
from tour.models import Tour, AvailableDate, Municipality, Deparment, TourCategory

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Tour, AvailableDate, Municipality, Deparment, TourCategory
from .forms import ReservaTourForm

class TourModelTest(TestCase):
    def setUp(self):
        # Crea instancias de prueba para los modelos relacionados
        municipality = Municipality.objects.create(name="Municipio de Prueba")
        department = Deparment.objects.create(name="Departamento de Prueba")
        category = TourCategory.objects.create(name="Aventura")

        # Crea un tour de prueba
        self.tour = Tour.objects.create(
            name="Tour de Prueba",
            description="Descripción de prueba",
            municipality=municipality,
            deparment=department,
            price=100.0
        )
        self.tour.categories.add(category)

        # Crea algunas fechas disponibles y asígnalas al tour
        fecha1 = AvailableDate.objects.create(date="2024-01-01")
        fecha2 = AvailableDate.objects.create(date="2024-02-01")
        self.tour.availableDate.add(fecha1, fecha2)

    def test_get_available_dates(self):
        # Llama al método y verifica que obtienes las fechas correctas
        fechas_disponibles = self.tour.get_available_dates()
    
        # Imprime los tipos de los elementos en `fechas_disponibles`
        print("Tipos de elementos en fechas_disponibles:", [type(fecha) for fecha in fechas_disponibles])

        fechas = [fecha.date for fecha in fechas_disponibles]  # Esto debería funcionar si los elementos son instancias de AvailableDate

        print("Fechas obtenidas por el método get_available_dates:", fechas)
        
