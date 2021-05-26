from django.forms import ModelForm
from diaryapp.models import Diary

class DiaryCreationForm(ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'feeling', 'date', 'content']