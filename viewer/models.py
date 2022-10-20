from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, \
    IntegerField


class Album(Model):
    name = CharField(max_length=128)


class Photo(Model):
    title = CharField(max_length=128)
    album_ID = ForeignKey(Album, on_delete=DO_NOTHING)
    width = IntegerField()
    height = IntegerField()
    color = CharField(max_length=18)
    URL = CharField(max_length=128)
