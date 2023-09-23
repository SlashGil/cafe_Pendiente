from django import forms
from django.forms import ModelForm

from coffee.variables.ModelsConstants import MAX_LENGTH_USER_NAME
from userManagement.models import User


class SignIn(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']
        widgets = {
            'name': forms.CharField(max_length=MAX_LENGTH_USER_NAME),
            'password': forms.PasswordInput()
        }
