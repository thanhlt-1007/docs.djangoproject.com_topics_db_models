from django.db.models import Model, ManyToManyField

from app.models import Topping


class Pizza(Model):
    toppings = ManyToManyField(to=Topping)
