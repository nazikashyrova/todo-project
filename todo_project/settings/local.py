import os

from todo_project.settings import BASE_DIR

DEBUG = True
ALLOWED_HOSTS = ['*']
#

SECRET_KEY = 'django-insecure-4bl$&pyz&7%scvqtb-)^+&n!iy9qv4ohma=(z^xwf60*)vc2y2'
SHARE_URL = "http://127.0.0.1:8000"
# Static assets
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)
# User uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')