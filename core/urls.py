from django.contrib import admin
from django.urls import path, include

# Personal views
from . import views

app_name = "core"

urlpatterns = [
    path("index", view=views.index_view.as_view(), name="idx")
]
