from django.db.models import Model, CharField, ManyToManyField

from app.models import Person


class Group(Model):
    name = CharField(max_length=128)

    members = ManyToManyField(to=Person, through="Membership")
