from django import template

register = template.Library()

@register.filter
def split_sentences(value):
    return value.split('\n')
