from django.db.models import Model, CharField


class Group(Model):
    name = CharField(max_length=128)
