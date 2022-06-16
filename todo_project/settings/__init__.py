from .base import *
import os


if os.environ.get("venv") == 'Production':
    from .production import *
else:
    from .local import *