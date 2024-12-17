from django.db.models import Model, ForeignKey, CASCADE
from app.models import Manufacturer


class Car(Model):
    manufacturer = ForeignKey(to=Manufacturer, on_delete=CASCADE)
