from django import forms
from car_check.models import car_fuel


class CarAddForm(forms.Form):
    mark = forms.CharField(label="Marka auta", max_length=50)
    car_model = forms.CharField(label="Model auta")
    engine = forms.IntegerField(label="Pojemność silnika")
    fuel = forms.ChoiceField(label="Rodzaj Paliwa", choices=car_fuel)
    vintage = forms.IntegerField(label="Rocznik")
    course = forms.IntegerField(label="Przebieg")
