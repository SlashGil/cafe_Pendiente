from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from userManagement.models import User


# Create your views here.
class CreateUser(LoginRequiredMixin, CreateView):
    model = User
    fields = ['email', 'first_name', 'last_name', 'password']
    template_name = 'create_user.html'
    success_url = reverse_lazy('home')


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')
