import dj_database_url
from carzone.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = '36z-*_ex9*e=%pjn4dly2l4qj$^eu^o1r$au&6tf1k30mu_%ca'

ALLOWED_HOSTS = ['blooming-river-97265.herokuapp.com']

DATABASES['default'] = dj_database_url.config()
