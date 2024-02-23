from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "product"

urlpatterns = [
    path("detail", view=views.product_detail_view.as_view(), name="detail")
]
