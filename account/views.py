from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic  import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import  SignUpForm
from django.urls import reverse_lazy


# Create your views here.

class SignUpView(CreateView):
    model = get_user_model()
    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')
