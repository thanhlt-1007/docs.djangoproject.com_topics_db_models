from django.db.models import Model, CharField, TextField


class Blog(Model):
    name = CharField(max_length=100)
    tagline = TextField()

    def save(self, **kwargs):
        if self.name == "Yoko Ono's blog":
            return
        else:
            super().save(**kwargs)
