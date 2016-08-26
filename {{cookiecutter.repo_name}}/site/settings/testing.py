import tempfile

from .base import *    # noqa

DEBUG = False

LANGUAGE_CODE = 'en'

MEDIA_ROOT = tempfile.mkdtemp()
