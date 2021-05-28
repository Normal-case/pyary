from django.urls import path
from diaryapp.views import *

app_name = 'diaryapp'
urlpatterns = [
    path('<str:id>', HomeView.as_view(), name='home'),
    path('create/<str:id>', DiaryCreate.as_view(), name='create'),
    path('read/<int:pk>', DiaryRead.as_view(), name='read'),
]