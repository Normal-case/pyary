from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accountapp.forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.urls import reverse

# Create your views here.
class AccountCreateView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'

class MyLoginView(LoginView):
    template_name = 'accountapp/login.html'

    def get_success_url(self):
        print(self.request.user.username)
        return reverse('profileapp:main', kwargs={'id':self.request.user.username})