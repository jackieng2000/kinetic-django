# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def multiply(value, factor):
    """Multiply value by a factor."""
    try:
        return float(value) * float(factor)
    except (ValueError, TypeError):
        return 0