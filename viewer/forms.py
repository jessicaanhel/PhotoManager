import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django.core.exceptions import ValidationError
from django.forms import CharField, IntegerField, ModelForm, ImageField, URLField

from viewer.models import Photo


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PhotoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            Row(Column('title'),
                Column('albumId')),
            'url',
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Photo
        fields = '__all__'

    title = CharField(validators=[capitalized_validator])
    albumId = IntegerField(min_value=1, max_value=4)
    url = URLField()
    thumbnailUrl = ImageField()

    def clean_url(self):
        initial = self.cleaned_data['url']
        sentences = re.sub(r'\s*\.\s*', '', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)