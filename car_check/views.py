from django.shortcuts import render
from django.views import View
from .forms import CarAddForm, WorkshopAddForm, OwnerAddForm, RepairAddForm
from .models import Car, Workshop, Owner, Repair


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
        form = OwnerAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            car = form.cleaned_data['car']

            owner_add = Owner.objects.create(name=name, last_name=last_name)
            owner_add.car.add(car)

            return render(request, "owner_add.html", {'owner_add': owner_add, 'car': car})


class RepairAddView(View):
    def get(self, request):
        form = RepairAddForm()
        return render(request, "repair_add.html", {'form': form})

    def post(self, request):
        form = RepairAddForm(request.POST)
        if form.is_valid():
            type_repair = form.cleaned_data['type_repair']
            description = form.cleaned_data['description']
            cost = form.cleaned_data['cost']
            car = form.cleaned_data['car']
            workshop = form.cleaned_data['workshop']

            repair_add = Repair.objects.create(type=type_repair, description=description, cost=cost,
                                               car=car,
                                               workshop=workshop)

            return render(request, "repair_add.html", {'repair_add': repair_add})
