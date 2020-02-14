from django import forms
from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserCreation(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'email']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']