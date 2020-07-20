from .settings import *
import dj_database_url

DEGUB = False

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['error-central-cn.herokuapp.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
