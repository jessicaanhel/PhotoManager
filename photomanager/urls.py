from django.contrib import admin
from django.urls import path

from viewer.views import test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', test_view)
]