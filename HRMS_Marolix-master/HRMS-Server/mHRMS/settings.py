from pathlib import Path
import datetime
import psycopg2
from decouple import config
import cloudinary_storage


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('django-insecure-#cedo6k@mkcoy%!r2$wy$8h-(9x&ev+v%tvx+-k-o%)2jt$fb^', default='your_default_secret_key_here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['3.87.139.193','*']

AUTH_USER_MODEL = "AdminAccount.User"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AdminAccount',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'mHRMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mHRMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config('NewServerrrrrr'),
       'USER': config('postgres'),
       'PASSWORD': config('uuuu1111'),
       'HOST': config('3.87.139.193'),
       'PORT': config('5432'),
   }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=360),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
}

CORS_ALLOW_ALL_ORIGINS = True

EMAIL_BACKEND = config('django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('smtp.elasticemail.com')
EMAIL_PORT = config('2525', default=25, cast=int)
EMAIL_USE_TLS = config('True', default=True, cast=bool)
EMAIL_USE_SSL = config('False', default=False, cast=bool)
EMAIL_HOST_USER = config('hrms.marolix@gmail.com')
EMAIL_HOST_PASSWORD = config('72A1E73834FF483792ED9D18912D7E32BB85')
DEFAULT_FROM_EMAIL = config('hrms.marolix@gmail.com')


#IMAGE UPLOAD
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dgjjuwjim',
    'API_KEY': '243264357325888',
    'API_SECRET': 'QFZd2KRDkm5wTB7s06KZ1UHH1F4'
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
