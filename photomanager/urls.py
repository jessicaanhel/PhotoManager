from django.contrib import admin
from django.urls import path, include

from viewer.models import Album, Photo
from viewer.views import IndexView

admin.site.register(Photo)
admin.site.register(Album)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('viewer/', include('viewer.urls', namespace='viewer'))
]
