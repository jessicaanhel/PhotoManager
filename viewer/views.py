from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django_tables2 import SingleTableView




from django.urls import reverse_lazy

from viewer.models import Photo
from viewer.forms import PhotoForm
from viewer.tables import PhotoTable


class PhotoListView(SingleTableView):
    model = Photo
    table_class = PhotoTable
    template_name = 'photo_list.html'


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo


class PhotoCreateView(CreateView):
    template_name = 'form.html'
    form_class = PhotoForm
    success_url = reverse_lazy('viewer:photo_list')


class PhotoUpdateView(UpdateView):
    template_name = 'form.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('viewer:photo_list')


class PhotoDeleteView(DeleteView):
    template_name = 'photo_confirm_delete.html'
    model = Photo
    success_url = reverse_lazy('viewer:photo_list')


class IndexView(PhotoListView):
    template_name = 'index.html'
