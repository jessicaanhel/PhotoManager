from django.contrib import admin
from django.urls import path

from viewer.models import Album, Photo
from viewer.views import IndexView

admin.site.register(Album)
admin.site.register(Photo)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
]