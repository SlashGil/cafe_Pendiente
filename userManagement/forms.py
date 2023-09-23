from django.forms import ModelForm

from userManagement.models import User


class SignIn(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']