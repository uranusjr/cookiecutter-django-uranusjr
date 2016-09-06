from .base import *     # noqa


DEBUG = True

INSTALLED_APPS += [     # noqa
    'debug_toolbar',
    'djgunicorn',
]

MIDDLEWARE += [     # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
