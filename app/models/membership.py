from django.db.models import Model, ForeignKey, CASCADE, DateField, CharField

from app.models import Person, Group


class Membership(Model):
    member = ForeignKey(to=Person, on_delete=CASCADE)
    group = ForeignKey(to=Group, on_delete=CASCADE)
    joined_date = DateField()
    invite_reason = CharField(max_length=64)
