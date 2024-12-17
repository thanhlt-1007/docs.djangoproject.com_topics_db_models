from django.db.models import Model, ForeignKey, CASCADE
from app.models import Manufacturer


class Car(Model):
    company_that_makes_it = ForeignKey(to=Manufacturer, on_delete=CASCADE)
