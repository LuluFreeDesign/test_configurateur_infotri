from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def infotri_script_url():
    base = getattr(settings, "BASE_URL", "")
    return f"{base}/infotri/iframe.js"


@register.simple_tag
def infotri_asl_script_url():
    base = getattr(settings, "BASE_URL", "")
    return f"{base}/infotri-asl/iframe.js"
