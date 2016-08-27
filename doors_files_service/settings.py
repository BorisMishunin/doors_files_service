# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'doors_files_service',
)

MIDDLEWARE_CLASSES = (
)

ROOT_URLCONF = 'doors_files_service.urls'

WSGI_APPLICATION = 'doors_files_service.wsgi.application'


#TEMPLATES = [
#]

# Database
#DATABASES = {
#}

# Internationalization

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = 'media/'

FORCE_SCRIPT_NAME = ''
