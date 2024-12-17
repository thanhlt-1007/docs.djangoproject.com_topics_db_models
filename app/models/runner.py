from django.db.models import Model, CharField, TextChoices


class Runner(Model):
    MedalType = TextChoices("MedalType", "GOLD SILVER BRONZE")

    name = CharField(max_length=60)
    medal = CharField(max_length=10, blank=True, choices=MedalType)
