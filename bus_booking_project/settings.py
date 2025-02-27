"""
Django settings for bus_booking_project project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aa5^2pqtkocjb+z0$vt^xho285hg15%ab%h-3m0m@whi4aso@b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bus_booking',
    'crispy_forms',
    'django.contrib.sites',  
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'widget_tweaks',

]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Important for language switching

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

ROOT_URLCONF = 'bus_booking_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Ensure templates directory is added
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
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "bus_booking/static",  # Ensure this points to the correct static directory
]

WSGI_APPLICATION = 'bus_booking_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'hr'
TIME_ZONE = 'Europe/Zagreb'  # Adjusting time zone to Croatia
LANGUAGE_CODE = 'hr'  # Default language (Croatian)
USE_I18N = True
USE_L10N = True
USE_TZ = True


from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('hr', _('Croatian')),
    ('en', _('English')),
    ('de', _('German')),
]
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server address
EMAIL_PORT = 587  # Or 465 for SSL
EMAIL_USE_TLS = True  # Or EMAIL_USE_SSL = True if using SSL
EMAIL_HOST_USER = 'aqdaszulfiqar30@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'fqhy ghjj gdbl taux'  # Your email password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'bus_booking:index'  # Redirects to homepage after login
LOGOUT_REDIRECT_URL = 'bus_booking:index'
