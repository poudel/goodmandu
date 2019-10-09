from .base import *


ALLOWED_HOSTS = ["*"]

ADMIN_URL = "admin/"

INTERNAL_IPS = ["127.0.0.1"]


# if DEBUG:
#     INSTALLED_APPS += ['debug_toolbar']
#     MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'goodmandu',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}

SITE_NAME = "goodmandu"
