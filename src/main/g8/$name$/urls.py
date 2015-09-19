#
# $name$ URL Configuration
#

from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    #
    url(r'^\$', 'apps.top.views.welcome'),
    url(r'^about/\$', 'apps.top.views.about'),
]


if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    urlpatterns += [
        url(r'^admin/', include(admin.site.urls))
    ]
