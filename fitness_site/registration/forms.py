from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Никнейм (нужен для логина)', widget=forms.TextInput(attrs={'class': 'username'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'username'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'username'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password', 'name': 'password'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'password', 'name': 'password'})) 
    avatar = forms.ImageField(label='Аватарка (необязательно)', required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'avatar')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Никнейм', widget=forms.TextInput(attrs={'class': 'username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password'}))
