from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '사용자이름'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'패스워드'}) 
        self.fields['password'].label = False

class SignUpForm(UserCreationForm):
    error_messages = {'password_mismatch':_('비밀번호가 일치하지 않습니다.')}
    username = forms.CharField(
        error_messages={'unique':_('이미 존재하는 아이디입니다.')},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '사용자아이디', 'label':''}), label='사용자아이디')
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}), label='비밀번호')
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 확인'}), label='비밀번호 확인')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일'}), label='이메일')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields