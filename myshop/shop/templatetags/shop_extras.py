from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Get value from dictionary by key in template: dict|get_item:key"""
    if not dictionary:
        return None
    try:
        return dictionary.get(key)
    except Exception:
        return None
