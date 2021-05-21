from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.forms import LoginForm
from accountapp.views import *

app_name = 'accountapp'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html', authentication_form=LoginForm), name='login'),
    path('create/', AccountCreateView.as_view(), name='create'),
]