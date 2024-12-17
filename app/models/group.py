from django.db.models import Model, CharField, ManyToManyField


class Group(Model):
    name = CharField(max_length=128)

    members = ManyToManyField(to="app.Person", through="app.Membership")
