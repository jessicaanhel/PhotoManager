from django.shortcuts import render
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from django.urls import reverse_lazy

from viewer.models import Photo
from viewer.forms import PhotoForm


def photos(request):
    s1 = request.GET.get('s1, ''')
    return render(
        request, template_name='photos.html',
        context={'photos': Photo.objects.all()})


class PhotoListView(ListView):
    template_name = 'photo_list.html'
    model = Photo


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
