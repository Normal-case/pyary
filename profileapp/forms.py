from django.forms import ModelForm
from django import forms
from profileapp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'phone_number', 'birth', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)
        self.fields['birth'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ex)2000-01-01'})
        self.fields['phone_number'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ex)"-" 빼고 작성해주세요'})
        self.fields['nickname'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':' '})