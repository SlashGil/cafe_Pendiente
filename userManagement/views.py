from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from userManagement.forms import SignIn
from userManagement.models import User


# Create your views here.
def CreateUser(request):
    if request.method == 'POST':
        user = request.POST
        userToSave = User(email=user.get('email'),
                          name=user.get('name'),
                          username=user.get('username'),
                          password=user.get('password'))
        userToSave.save()
        return redirect('/')
    else:
        context = {}
        context['form'] = SignIn()
        return render(request,'registration/signin.html',context)

