from .settings import*

DEBUG = True
#Crie secret key para seu ambiente de desenvolvimento
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_XWL8oQ9MJCvl',
        'HOST': 'ep-sparkling-rain-a8v31umy-pooler.eastus2.azure.neon.tech',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}