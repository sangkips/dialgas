from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from .models import Consumer, Supplier, Estate

from .forms import SignupForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    user = request.user
    suppliers = Supplier.objects.filter(owner=user)
    prof = Consumer.objects.get(name__id=user.id)
    return render(request, 'profile.html', {'prof': prof, 'user': user, 'suppliers': suppliers})
