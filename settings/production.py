import debug_toolbar

from .base import *

DEBUG = False

INSTALLED_APPS+= ["dbbackup"]

ALLOWED_HOSTS = ['herokuapp.com']

ADMINS = [("Nazik", "nazikashyrowa@gmail.com")]