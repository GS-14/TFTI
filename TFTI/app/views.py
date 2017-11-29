# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from app.forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.age = form.cleaned_data.get('age')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, firstname = user.first_name, lastname = user.last_name, password=raw_password)
            login(request, user)
            #return redirect('dashboard')
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})