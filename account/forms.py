from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class SignUpForm(UserCreationForm):
    email =forms.EmailField()
    groups = forms.ChoiceField()
    class Meta:
        model = Profile
        fields = ['username', 'password1','password2', 'email', 'groups' ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'age', 'gender', 'image', 'about', 'phone_number' ]
