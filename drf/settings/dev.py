from .base import * # noqa
# from django.conf.settings import *

# SECRET_KEY = '$7x^8fgxa-%3nrhuw(lx&*@w(8=m!1s5a!78aqy8oz8t2+h$_v'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

ALLOWED_HOSTS = ['0.0.0.0']
