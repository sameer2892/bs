import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default':{
        'ENGINE':'django.contrib.gis.db.backends.postgis',
        'NAME':'binaryscript'
    }
}

BASE_URL='http://192.168.100.2:8000'
IS_TEST=True
AUTH_USERNAMES = [
    '9833371069',
]
ADMINS = (
    ('Anurag Meena', 'anuragmeena92@gmail.com'),
)
# STATICFILES_STORAGE='django_s3_storage.storage.StaticS3Storage'
STATIC_ROOT = os.path.join(BASE_DIR, 'app/static/')
STATICFILES_LOCATION = 'static'
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'app/static/media')


SERVER_DOMAIN = 'http://localhost:8000/'