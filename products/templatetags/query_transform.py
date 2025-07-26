# products/templatetags/query_transform.py
from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    """
    Returns the URL-encoded querystring for the current request,
    updating the parameters with the key/value pairs passed to the tag.
    """
    request = context.get('request')
    if not request:
        return ''
    
    updated = request.GET.copy()
    for key, value in kwargs.items():
        if value is None:
            if key in updated:
                del updated[key]
        elif key == 'remove':
            if value in updated:
                del updated[value]
            elif value in updated.getlist('method'):
                methods = updated.getlist('method')
                methods.remove(value)
                updated.setlist('method', methods)
        else:
            updated[key] = value
            
    return updated.urlencode()