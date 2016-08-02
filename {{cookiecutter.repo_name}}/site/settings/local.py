from .base import *     # noqa


DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
    'djgunicorn',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
