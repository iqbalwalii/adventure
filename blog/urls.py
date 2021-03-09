from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('/blog', TemplateView.as_view(), name='blog'),
]
