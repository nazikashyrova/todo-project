from .base import *

DEBUG = False
INSTALLED_APPS += (
    # other apps for production site
)
INSTALLED_APPS += ["dbbackup"]

ALLOWED_HOSTS = ['herokuapp.com']

ADMINS = [("Nazik", "nazikashyrowa@gmail.com")]

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'media'
