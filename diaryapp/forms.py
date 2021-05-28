from django.forms import ModelForm
from django.forms.widgets import MediaOrderConflictWarning
from diaryapp.models import Diary
from django import forms
from memory_storage import settings

class DiaryCreationForm(ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'feeling', 'date', 'ocr_image', 'content']
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        }