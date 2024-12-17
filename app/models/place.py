from django.db.models import Model, CharField


class Place(Model):
    name = CharField(max_length=50)
    address = CharField(max_length=100)
