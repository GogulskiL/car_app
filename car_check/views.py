from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from .forms import CarAddForm, WorkshopAddForm, OwnerAddForm
from .models import Car, Workshop, Owner


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class CarAddView(View):
    def get(self, request):
        form = CarAddForm()
        return render(request, "car_add.html", {'form': form})

    def post(self, request):
        form = CarAddForm(request.POST)
        if form.is_valid():
            car = form.cleaned_data['mark']
            model = form.cleaned_data['car_model']
            engine = form.cleaned_data['engine']
            fuel = form.cleaned_data['fuel']
            vintage = form.cleaned_data['vintage']
            course = form.cleaned_data['course']
            car_add = Car.objects.create(mark=car, car_model=model, engine=engine, fuel=fuel, vintage=vintage,
                                         course=course)
            return render(request, 'car_add.html', {'car_add': car_add})


class WorkshopAddView(View):
    def get(self, request):
        form = WorkshopAddForm()
        return render(request, "workshop_add.html", {'form': form})

    def post(self, request):
        form = WorkshopAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            note = form.cleaned_data['note']
            prices = form.cleaned_data['prices']
            short_description = form.cleaned_data['short_description']
            workshop_add = Workshop.objects.create(name=name, phone_number=phone_number, address=address, note=note,
                                                   prices=prices, short_description=short_description)

            return render(request, "workshop_add.html", {'workshop_add': workshop_add})


class OwnerAddView(View):
    def get(self, request):
        form = OwnerAddForm()
        return render(request, "owner_add.html", {'form': form})

    def post(self, request):
        pass
