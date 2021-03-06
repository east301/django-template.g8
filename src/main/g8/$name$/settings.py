#
# Django settings for $name$ project.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/1.8/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.8/ref/settings/
#
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
#

# ================================================================================
# Local settings
# ================================================================================

from .settings_local import *  # NOQA


# ================================================================================
# Path
# ================================================================================

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ================================================================================
# Django applications & middlewares
# ================================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'widget_tweaks',

    'apps.front',
) + ADDITIONAL_INSTALLED_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


# ================================================================================
# URL routing
# ================================================================================

ROOT_URLCONF = '$name$.urls'


# ================================================================================
# WSGI
# ================================================================================

WSGI_APPLICATION = '$name$.wsgi.application'


# ================================================================================
# Template
# ================================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'assets', 'templates')
        ],
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


# ================================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# ================================================================================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets', 'components'),
]


# ================================================================================
# Security
# ================================================================================

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True


# ================================================================================
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
# ================================================================================

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = False
USE_L10N = False
USE_TZ = True
