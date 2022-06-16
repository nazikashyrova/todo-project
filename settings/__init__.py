from .base import *
import os


if os.environ.get("venv") == 'prod':
    from .production import *
else:
    from .local import *
