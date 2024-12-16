from django.db.models import Model, CharField


class Person(Model):
    SHIRT_SIZES = {"S": "Small", "M": "Medium", "L": "Large"}

    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    shirt_size = CharField(max_length=1, choices=SHIRT_SIZES, default="S")
