from django.db.models import Model, CharField, PositiveIntegerField


class CommonInfo(Model):
    name = CharField(max_length=100)
    age = PositiveIntegerField()

    class Meta:
        abstract = True
