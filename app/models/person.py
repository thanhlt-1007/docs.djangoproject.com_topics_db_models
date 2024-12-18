from django.db.models import Model, CharField, DateField, ManyToManyField

from django.utils import timezone


class Person(Model):
    SHIRT_SIZES = {"S": "Small", "M": "Medium", "L": "Large"}

    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    shirt_size = CharField(max_length=1, choices=SHIRT_SIZES, default="S")
    birth_date = DateField(default=timezone.now)

    groups = ManyToManyField(to="app.Group", through="app.Membership")

    def baby_boomer_status(self):
        from datetime import date

        if self.birth_date < date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date > date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
