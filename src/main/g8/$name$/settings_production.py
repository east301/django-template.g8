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
# Path
# ================================================================================

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ================================================================================
# Debugging mode
# ================================================================================

DEBUG = False
ALLOWED_HOSTS = []


# ================================================================================
# Django applications & middlewares
# ================================================================================

ADDITIONAL_INSTALLED_APPS = (
)


# ================================================================================
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '$name$'
    }
}


# ================================================================================
# Security
# ================================================================================

SECRET_KEY = '$secretKeyPrefix;format="random"$'
