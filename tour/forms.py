from django import forms
from .models import Deparment, TourCategory, Municipality,AvailableDate


class BusquedaTourForm(forms.Form):
    category = forms.ModelChoiceField(queryset=TourCategory.objects.all(), required=False, label="Categoría")
    deparment = forms.ModelChoiceField(queryset=Deparment.objects.all(), required=False, label="Departamento")
    municipality = forms.ModelChoiceField(queryset=Municipality.objects.all(), required=False, label="Municipio")
    price_min = forms.FloatField(required=False, label="Precio Mínimo")
    price_max = forms.FloatField(required=False, label="Precio Máximo")



class ReservationForm(forms.Form):
    date = forms.ModelChoiceField(queryset=AvailableDate.objects.all(), label="Fecha Disponible", widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
    people = forms.IntegerField(min_value=1, label="Cantidad de Personas")

    def __init__(self, *args, **kwargs):
        tour = kwargs.pop('tour', None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        if tour:
            self.fields['date'].queryset = tour.availableDate.all()


