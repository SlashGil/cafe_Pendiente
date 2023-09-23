from django import forms
from django.forms import ModelForm

from coffee.variables.ModelsConstants import MAX_LENGTH_USER_NAME, MAX_LENGTH_PASSWORD
from userManagement.models import User


class SignIn(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=MAX_LENGTH_USER_NAME)
    username = forms.CharField(max_length=MAX_LENGTH_USER_NAME)
    password = forms.CharField(max_length=MAX_LENGTH_PASSWORD, widget=forms.PasswordInput)

