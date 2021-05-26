from django.urls import path
from diaryapp.views import *

app_name = 'diaryapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', DiaryCreate.as_view(), name='create'),
]