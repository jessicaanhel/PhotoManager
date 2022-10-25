from django.db.models import CharField, Model, IntegerField, ImageField


class Photo(Model):
    title = CharField(max_length=128)
    album_ID = IntegerField()
    # i didnt know , i need to create additional model and connect it with
    # fierign key. But if i havent any album data instead id in jsonholder,
    # I will create standart integer.
    width = IntegerField()
    height = IntegerField()
    color = CharField(max_length=18)
    url = ImageField(max_length=128)
    thumbnailUrl = ImageField(max_length=128)
