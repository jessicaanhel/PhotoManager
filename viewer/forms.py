import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django.core.exceptions import ValidationError
from django.forms import CharField, IntegerField, ModelForm

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
            Row(Column('album_ID'), Column('width'), Column('height'),
                Column('url'), Column('thumbnailUrl')),
            'color',
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Photo
        fields = '__all__'

    title = CharField(validators=[capitalized_validator])
    width = IntegerField(min_value=1, max_value=4)
    height = IntegerField(min_value=1, max_value=4)
    color = CharField(max_length=18)
    url = CharField(max_length=128)
    thumbnailUrl = CharField(max_length=128)

    def clean_url(self):
        initial = self.cleaned_data['URL']
        sentences = re.sub(r'\s*\.\s*', '', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)