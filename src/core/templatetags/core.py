import re
from django import template
from markdown2 import markdown

register = template.Library()


@register.filter
def mdown(content):
    return markdown(content or "")


DOMAIN_REGEX = re.compile(r"https?://(?P<domain>[a-zA-Z0-9.]+)/?")


@register.filter
def domain(url):
    if url:
        match = DOMAIN_REGEX.match(url)
        if match:
            return match.groupdict()['domain']
    return url
