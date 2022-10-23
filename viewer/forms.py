import re
from datetime import date

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django.core.exceptions import ValidationError
from django.forms import CharField, DateField, IntegerField, ModelForm

from viewer.models import Photo


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class PhotoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            Row(Column('album_ID'), Column('width'), Column('height'),
                Column('URL')),
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
    URL = CharField(max_length=128)

    def clean_url(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['URL']
        sentences = re.sub(r'\s*\.\s*', '', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)