from django.db.models import Model, CharField


class Fruit(Model):
    name = CharField(max_length=100, primary_key=True)
