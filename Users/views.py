from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView

# Create your views here.


class Register(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_message = 'Created Successfully'

    def get(self, request):
        return render(request, self.template_name, {'form': form_class})
