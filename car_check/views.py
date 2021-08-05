from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CarAddForm, WorkshopAddForm, OwnerAddForm, RepairAddForm, CarRemoveForm, WorkshopRemoveForm, \
    OwnerRemoveForm, RepairRemoveForm
from .models import Car, Workshop, Owner, Repair


class HomeView(View):
    """
    Return home views. 
    """
    def get(self, request):
        car_last = Car.objects.all().reverse()[0]
        workshop_last = Workshop.objects.all().reverse()[0]
        owner_last = Owner.objects.all().reverse()[0]
        repair_last = Repair.objects.all().reverse()[0]
        ctx = {
            'car_last': car_last,
            'workshop_last': workshop_last,
            'owner_last': owner_last,
            'repair_last': repair_last
        }
        return render(request, "index.html", ctx)


class CarAddView(View):
    def get(self, request):
        """
        Return form add car.
        """
        form = CarAddForm()
        return render(request, "car_add.html", {'form': form})

    def post(self, request):
        """
        Return cleaned data from forms add car
        """
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


class CarRemoveView(View):
    def get(self, request):
        form = CarRemoveForm()
        return render(request, 'car_remove.html', {'form': form})

    def post(self, request):
        form = CarRemoveForm(request.POST)
        if form.is_valid():
            car = form.cleaned_data['car']
            remove_car = Car.objects.get(id=car.id)
            remove_car.delete()
            return HttpResponse("<p> Usunięte <p>")


class CarAllView(View):
    def get(self, request):
        car = Car.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(car, 5)
        try:
            car = paginator.page(page)
        except PageNotAnInteger:
            car = paginator.page(1)
        except EmptyPage:
            car = paginator.page(paginator.num_pages)
        return render(request, "car_all.html", {'car': car})


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


class WorkshopRemoveView(View):
    def get(self, reguest):
        form = WorkshopRemoveForm()
        return render(reguest, "workshop_remove.html", {'form': form})

    def post(self, request):
        form = WorkshopRemoveForm(request.POST)
        if form.is_valid():
            workshop = form.cleaned_data['workshop']
            workshop_remove = Workshop.objects.get(id=workshop.id)
            workshop_remove.delete()
            return HttpResponse("<p>Usunięto</p>")


class WorkshopAllView(View):
    def get(self, request):
        workshop = Workshop.objects.all()
        return render(request, 'workshop_all.html', {'workshop': workshop})


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


class OwnerRemoveView(View):
    def get(self, request):
        form = OwnerRemoveForm()
        return render(request, "owner_remove.html", {'form': form})

    def post(self, request):
        form = OwnerRemoveForm(request.POST)
        if form.is_valid():
            owner = form.cleaned_data['owner']
            owner_remove = Owner.objects.get(id=owner.id)
            owner_remove.delete()
            return HttpResponse("<p>Usunięte<p>")


class OwnerAllView(View):
    def get(self, request):
        owner = Owner.objects.all()
        return render(request, "owner_all.html", {'owner': owner})


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
            ctx = {
                'repair_add': repair_add,
                'car': car,
                'workshop': workshop
            }
            return render(request, "repair_add.html", ctx)


class RepairRemoveView(View):
    def get(self, request):
        form = RepairRemoveForm()
        return render(request, "repair_remove.html", {'form': form})

    def post(self, request):
        form = RepairRemoveForm(request.POST)
        if form.is_valid():
            repair = form.cleaned_data['repair']
            repair_remove = Repair.objects.get(id=repair.id)
            repair_remove.delete()
            return HttpResponse("<p>Usunięto<p>")


class RepairAllView(View):
    def get(self, request):
        repair = Repair.objects.all()
        return render(request, "repair_all.html", {'repair': repair})
