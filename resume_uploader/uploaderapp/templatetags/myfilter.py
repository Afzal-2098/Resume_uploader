from django import template
register = template.Library()

@register.filter(name='special_char')
def remove_char(value, arg):
    for character in arg:
        value = value.replace(character, "")
    return value
