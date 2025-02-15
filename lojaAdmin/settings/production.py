from .settings import *

DEBUG = False
#Crie a secret key para seu ambiente de produção
SECRET_KEY = 'ixb6fha#ts=&b4t2u%p1_62-!8dw2j==j)d^3-j$!z(@*m+-h'
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg',
        'NAME': 'neondb',
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_XWL8oQ9MJCvl',
        'HOST': 'ep-sparkling-rain-a8v31umy-pooler.eastus2.azure.neon.tech',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}