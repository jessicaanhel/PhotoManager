from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from viewer.models import Photo
from viewer.views import IndexView

admin.site.register(Photo)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('viewer/', include('viewer.urls', namespace='viewer')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
