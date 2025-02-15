from .settings import*

DEBUG = True
#Crie secret key para seu ambiente de desenvolvimento
SECRET_KEY='ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'
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