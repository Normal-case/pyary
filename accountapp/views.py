from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accountapp.forms import SignUpForm

# Create your views here.
class AccountCreateView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'