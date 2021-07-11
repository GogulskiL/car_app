from django.db import models

from django.db import models

car_fuel = (
    (1, "Benzyna"),
    (2, "Deisel"),
    (3, "Benzyna+LPG"),
    (4, "Elektryczne"),
)
rating = (
    (1, "słaby"),
    (2, "przeciętny"),
    (3, "średni"),
    (4, "dobry"),
    (5, "bardzo dobry"),
)
price_workshop = (
    (1, "tani"),
    (2, "średni"),
    (3, "drogi"),
)
type_of_repair = (
    (1, "silnik"),
    (2, "zawieszenie"),
    (3, "elektryka"),
    (4, "wulkanizacja"),
    (5, "wymianny okresowe"),
    (6, "inne"),
)


class Car(models.Model):
    """
    Car class description of the most important parameters
    """
    mark = models.CharField(max_length=64)
    car_model = models.CharField(max_length=64)
    engine = models.IntegerField()
    fuel = models.IntegerField(choices=car_fuel)
    vintage = models.IntegerField()
    course = models.IntegerField()

    def __str__(self):
        return self.mark + " " + self.car_model


class Workshop(models.Model):
    """
    Class of the workshop with information about the workshop
    """
    name = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=64)
    note = models.IntegerField(choices=rating)
    prices = models.IntegerField(choices=price_workshop)
    short_description = models.CharField(max_length=1000)


class Owner(models.Model):
    """
    User class linked to the car model and repair
    """
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    car = models.ManyToManyField(Car)


class Repair(models.Model):
    """
    Repair class with a description of repairs, combined with the car and workshop class
    """
    type = models.IntegerField(choices=type_of_repair)
    description = models.CharField(max_length=1000)
    date_repair = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)


class Remainder(models.Model):
    """
    Auxiliary class for reminders
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
