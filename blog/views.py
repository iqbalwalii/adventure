from django.shortcuts import render
from django.views.generic import ListView, View

# Create your views here.
from django.views.generic import TemplateView
from .models import Post
class PostView(ListView):
    template_name='blog.html'
    model = Post
    def get(self, request):
        return render(request, self.template_name, {'posts': Post.objects.all()})