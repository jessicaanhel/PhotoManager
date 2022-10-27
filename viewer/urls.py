from django.urls import path

from viewer.views import (
    IndexView, PhotoListView, PhotoDetailView, PhotoCreateView,
    PhotoUpdateView, PhotoDeleteView
)

app_name = 'viewer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/list', PhotoListView.as_view(), name='photo_list'),
    path('photo/detail/<pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/delete', PhotoListView.as_view(), name='photo_confirm_delete'),
    path('photo/update/<pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/delete/<pk>', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/create', PhotoCreateView.as_view(), name='photo_create'),
    ]
