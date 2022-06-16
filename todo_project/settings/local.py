import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar', # and other apps for local development
)

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
SECRET_KEY = 'django-insecure-4bl$&pyz&7%scvqtb-)^+&n!iy9qv4ohma=(z^xwf60*)vc2y2'

del STATIC_ROOT
ALLOWED_HOSTS = ['localhost', '127.0.0.1']