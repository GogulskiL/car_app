from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from .forms import CarAddForm
from .models import Car


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class CarAdd(View):
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
