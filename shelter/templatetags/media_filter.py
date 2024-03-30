from django import template

register = template.Library()


@register.filter
def media_filter(value):
    return f"/media/{value}"