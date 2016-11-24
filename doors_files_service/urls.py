from django.conf.urls import include, url
import doors_files_service.localsettings as settings
from django.contrib import admin
import views

admin.autodiscover()
urlpatterns = [
    url(r'^upload_file$',
        views.upload_file,
        name='upload_file'),
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns.append(
    (r'^' + settings.MEDIA_URL + '(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT})
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()