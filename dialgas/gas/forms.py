from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Consumer, Supplier
from django import forms

class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
