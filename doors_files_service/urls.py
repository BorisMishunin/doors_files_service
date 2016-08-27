from django.conf.urls import patterns, include, url
import doors_files_service.localsettings as settings

urlpatterns = patterns(
    '',
    url(r'^upload_file$',
        'doors_files_service.views.upload_file',
        name='upload_file'),
)


urlpatterns += patterns(
    '',
    (r'^' + settings.MEDIA_URL + '(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT})
)
