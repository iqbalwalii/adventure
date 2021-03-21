from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from django.views.generic import TemplateView
from .models import Posts

class BlogView(TemplateView):
    template_name='blog.html'
    context_object_name='web_posts'
    model=Posts
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

# class PostView(ListView):
#     template_name='blog.html'
    
