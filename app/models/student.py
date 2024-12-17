from django.db.models import CharField


from .common_info import CommonInfo


class Student(CommonInfo):
    home_group = CharField(max_length=5)
