from django import template

register = template.Library()

@register.filter
def get_type(value):
    return type(value)

@register.filter
def conv_str(value):
    return int(str.__str__(value))