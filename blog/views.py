from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name='blog.html'