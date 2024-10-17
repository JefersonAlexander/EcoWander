from django import forms
from .models import Deparment, TourCategory, Municipality


class BusquedaTourForm(forms.Form):
    category = forms.ModelChoiceField(queryset=TourCategory.objects.all(), required=False, label="Categoría")
    deparment = forms.ModelChoiceField(queryset=Deparment.objects.all(), required=False, label="Departamento")
    municipality = forms.ModelChoiceField(queryset=Municipality.objects.all(), required=False, label="Municipio")
    price_min = forms.FloatField(required=False, label="Precio Mínimo")
    price_max = forms.FloatField(required=False, label="Precio Máximo")