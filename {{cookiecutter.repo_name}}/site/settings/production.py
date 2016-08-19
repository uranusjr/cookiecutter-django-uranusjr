from .base import *     # noqa


DEBUG = False

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname).1s [%(name)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # TODO: Give me a better configuration.
            # 'filename': '{{ cookiecutter.repo_name }}.log',
            'maxBytes': 1024 * 1024,    # 1 MB.
            'backupCount': 10,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 0,
        'handlers': ['console', 'file'],
    }
}
