from django import template

register = template.Library()

@register.filter
def hyphenSpace(value):
    return value.replace("-", " ")