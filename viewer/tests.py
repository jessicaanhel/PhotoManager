from django.test import TransactionTestCase
from django.urls import reverse

from viewer.forms import PhotoForm
from viewer.models import Album, Photo


class TestViewer(TransactionTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    fixtures = ['fixtures.json']

    def test_cannot_create_photo_without_title_capitalization(self):
        self.client.login(username='creator', password='pass')
        data = {
            'title': 'the Imitation photo name',
            'album_ID': Album.objects.get(name='nazwa albumu').id,
            "width": 300,
            "height": 400,
            "color": "hex",
            "URL": "http:/"
        }
        self.client.post(reverse('viewer:photo_create'), data)
        actual_query = Photo.objects.filter(
            title__contains='Imitation photo name')
        self.assertFalse(actual_query.exists())

    def test_photo_form_rejects_data_without_title_capitalization(self):
        data = {
            'title': 'the Imitation photo name',
            'album_ID': Album.objects.get(name='nazwa albumu').id,
            "width": 300,
            "height": 400,
            "color": "hex",
            "URL": "http:/"
        }
        form = PhotoForm(data=data)
        self.assertFalse(form.is_valid())
