from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cursos_cidetec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^preregistro/',include('preregistro.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
