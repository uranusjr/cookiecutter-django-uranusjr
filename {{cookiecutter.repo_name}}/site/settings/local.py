from .base import *     # noqa


DEBUG = True

INSTALLED_APPS += [     # noqa
    'debug_toolbar',
    'djgunicorn',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_PATCH_SETTINGS = False
