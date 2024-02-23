from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

# Personal views
from . import views

app_name = "core"

urlpatterns = [
    path("index", view=views.index_view.as_view(), name="idx")
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]