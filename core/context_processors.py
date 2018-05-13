from django.conf import settings


def basic(request):
    return {
        "SITE_NAME": settings.SITE_NAME
    }
