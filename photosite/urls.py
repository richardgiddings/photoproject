from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'photosite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cat_filter/$', views.cat_filter, name='cat_filter'),
    url(r'^photo_search/$', views.photo_search, name='photo_search'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^cat_filter/media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^photo_search/media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]