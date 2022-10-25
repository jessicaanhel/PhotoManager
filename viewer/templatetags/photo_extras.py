from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString

register = Library()


@register.simple_tag
def photo_format(photo, short=False):
    if short:
        return f'{photo.title} ({photo.url})'
    return f'{photo.title} ({photo.color}) - {photo.albumId}'


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value}</p>')
