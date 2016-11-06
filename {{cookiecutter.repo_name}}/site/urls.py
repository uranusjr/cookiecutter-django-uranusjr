from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve as serve_static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve_static,
            {'document_root': settings.MEDIA_ROOT}),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
