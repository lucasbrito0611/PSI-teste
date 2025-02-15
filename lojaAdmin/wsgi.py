import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lojaAdmin.settings.development')

application = get_wsgi_application()

app = application