from django import template

register = template.Library()

def addClass(value, token):
    value.field.widget.attrs["class"] = token
    return value

def addPlaceholder(value, token):
    value.field.widget.attrs["placeholder"] = token
    return value

register.filter(addClass)
register.filter(addPlaceholder)