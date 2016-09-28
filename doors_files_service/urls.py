from django.conf.urls import patterns, include, url
import doors_files_service.localsettings as settings
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^upload_file$',
        'doors_files_service.views.upload_file',
        name='upload_file'),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns(
    '',
    (r'^' + settings.MEDIA_URL + '(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT})
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()