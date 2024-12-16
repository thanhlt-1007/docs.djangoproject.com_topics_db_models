from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    CharField,
    DateField,
    IntegerField,
)

from app.models import Musician


class Album(Model):
    artist = ForeignKey(to=Musician, on_delete=CASCADE)
    name = CharField(max_length=100)
    release_date = DateField()
    num_starts = IntegerField()
