import os
import sys
from pathlib import Path

# Directorio donde están settings.py y store/
PROJECT_DIR = Path(__file__).resolve().parent

# Permitir que Django encuentre la aplicación store
sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'techgear_web.settings'
)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()