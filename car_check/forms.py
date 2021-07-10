from django import forms
from car_check.models import car_fuel, rating, price_workshop, Car


class CarAddForm(forms.Form):
    mark = forms.CharField(label="Marka auta", max_length=50)
    car_model = forms.CharField(label="Model auta")
    engine = forms.IntegerField(label="Pojemność silnika")
    fuel = forms.ChoiceField(label="Rodzaj Paliwa", choices=car_fuel)
    vintage = forms.IntegerField(label="Rocznik")
    course = forms.IntegerField(label="Przebieg")


class WorkshopAddForm(forms.Form):
    name = forms.CharField(label="Nazwa warsztatu")
    phone_number = forms.IntegerField(label="Numer telefonu")
    address = forms.CharField(label="Adres")
    note = forms.ChoiceField(label="Ocena warsztatu", choices=rating)
    prices = forms.ChoiceField(label="Ceny warsztatu", choices=price_workshop)
    short_description = forms.CharField(label="Opis warsztatu")


class OwnerAddForm(forms.Form):
    name = forms.CharField(label="Imię")
    last_name = forms.CharField(label="Nazwisko")
    car = forms.ModelChoiceField(Car.objects.all())
