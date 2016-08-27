import os
import json
import logging

from .settings import *


DEBUG = True if os.environ.get('DJANGO_DEBUG', '') == 'true' else False

# Databases
DATABASES = json.load(open(os.environ['FILES_DB_CONFIG']))

# Loggers
try:
    LOGGING = json.load(open(os.environ['FILES_LOGGERS']))
except Exception, e:
    logging.exception(e)

# Sentry
if os.environ.get('FILES_SENTRY_URL'):
    RAVEN_CONFIG = {
        'dsn': os.environ.get('FILES_SENTRY_URL'),
    }
    INSTALLED_APPS += ( 'raven.contrib.django.raven_compat',)

# Debug mode
if DEBUG:
    INSTALLED_APPS += ('django.contrib.staticfiles',)


MEDIA_ROOT = os.environ['DOORS_FILES_MEDIA_ROOT']
WATERMARK_FONT_PATH = os.path.join(BASE_DIR, 'doors_files_service', 'CONSOLA.TTF')

