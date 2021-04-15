from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView
from .views import PostView

urlpatterns = [
    path('blog', PostView.as_view(template_name='blog/blog.html'), name='blog'),
]
