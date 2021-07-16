"""car_status URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from car_check.views import HomeView, CarAddView, WorkshopAddView, OwnerAddView, RepairAddView, CarRemoveView, \
    WorkshopRemoveView, OwnerRemoveView, RepairRemoveView, CarAllView, WorkshopAllView, OwnerAllView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_car/', CarAddView.as_view(), name='add-car'),
    path('car_remove/', CarRemoveView.as_view(), name='car-remove'),
    path('car_all/', CarAllView.as_view(), name='car-all'),
    path('workshop_add/', WorkshopAddView.as_view(), name='workshop-add'),
    path('workshop_remove/', WorkshopRemoveView.as_view(), name='workshop-remove'),
    path('workshop_all/', WorkshopAllView.as_view(), name='workshop-all'),
    path('owner_add/', OwnerAddView.as_view(), name='owner-add'),
    path('owner_remove', OwnerRemoveView.as_view(), name='owner-remove'),
    path('owner_all', OwnerAllView.as_view(), name='owner-all'),
    path('repair_add/', RepairAddView.as_view(), name='repair-add'),
    path('repair_remove/', RepairRemoveView.as_view(), name='repair-remove'),
]
