from django_tables2 import Table, LinkColumn
from viewer.models import Photo
from django_tables2.utils import A


class PhotoTable(Table):
    edit = LinkColumn('viewer:photo_update', text="Update", args=[A('pk')], orderable=False,
                             empty_values=())
    delete = LinkColumn('viewer:photo_delete', text="Delete", args=[A('pk')], orderable=False,
                             empty_values=())
    class Meta:
        model = Photo
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "title", "albumId", "width", "height", "color", "url")