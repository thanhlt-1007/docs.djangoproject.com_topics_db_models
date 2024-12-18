from app.models import Person


class MyPerson(Person):
    class Meta:
        proxy = True
