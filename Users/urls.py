from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register

urlpatterns = [
    path('signup/', Register.as_view(template_name='Users/register.html'), name='register'),
]
