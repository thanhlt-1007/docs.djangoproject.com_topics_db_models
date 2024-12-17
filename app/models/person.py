from django.db.models import Model, CharField, DateField, ManyToManyField

from django.utils import timezone


class Person(Model):
    SHIRT_SIZES = {"S": "Small", "M": "Medium", "L": "Large"}

    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    shirt_size = CharField(max_length=1, choices=SHIRT_SIZES, default="S")
    birth_date = DateField(default=timezone.now().date())

    groups = ManyToManyField(to="app.Group", through="app.Membership")
